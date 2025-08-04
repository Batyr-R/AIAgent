import os
import sys
from google import genai
from dotenv import load_dotenv
import argparse

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

prompt = arguments.prompt

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=prompt
)

if arguments.verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
