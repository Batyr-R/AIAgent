import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error: prompt not provided")
    sys.exit(1)

prompt = " ".join(sys.argv[1:])

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=prompt
)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
