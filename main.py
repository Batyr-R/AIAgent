import os
import sys
from google import genai
from dotenv import load_dotenv
import argparse
from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser()
parser.add_argument('prompt')
parser.add_argument('--verbose', action='store_true')
arguments = parser.parse_args()

if len(sys.argv) < 2:
    print("Error: prompt not provided")
    sys.exit(1)

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Gets required files content.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Relative path to the required file.",
            ),
        },
    ),
)

schema_run_python_file = genai.types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Path to the executed python file.",
            ),

        },
    ),
)

schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Writes and overwrites files.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Path to the file being edited.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Content, that is being written."
            )
        },
    ),
)



available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

spell_book = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_call_part.args["working_directory"] = "./calculator"
    if function_call_part.name not in spell_book:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    result = spell_book[function_call_part.name](**function_call_part.args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )

prompt = arguments.prompt
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=prompt,
    config=genai.types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    ),
)

if arguments.verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

for p in response.candidates[0].content.parts:
    if p.function_call != None:
        content = call_function(p.function_call, arguments.verbose)
        if content.parts[0].function_response.response != None and arguments.verbose:
            print(f"-> {content.parts[0].function_response.response}")
        else:
            raise Exception("FATAL: u a bum")
    else:
        print(p.text)
