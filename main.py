import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) <= 1:
        print("Error: Please provide a prompt as a command line argument.", file=sys.stderr)
        sys.exit(1)
    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=messages
    )
    usage = response.usage_metadata

    if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
        print(f"User prompt: {prompt}")
    
    print(response.text)
    if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}") 


if __name__ == "__main__":
    main()
