from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os
from dotenv import load_dotenv

def call_claude(prompt):
        
    load_dotenv() # looks for .env file
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    anthropic = Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key = api_key,
    )

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=prompt,
    )
    return completion.completion

def main():
    prompt = f"{HUMAN_PROMPT} how does a court case get to the Supreme Court?{AI_PROMPT}"
    print(call_claude(prompt))


if __name__ == "__main__":
    main()
