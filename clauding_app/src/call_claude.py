from anthropic import Anthropic
import os
from dotenv import load_dotenv


def call_claude(prompt_txt):
        
    load_dotenv() # looks for .env file
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    anthropic = Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key = api_key,
    )

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=90000,
        prompt=prompt_txt,
    )

    return completion.completion
