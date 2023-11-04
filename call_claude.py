from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os
from dotenv import load_dotenv


def call_claude(prompt_instructions, codebase_txt):
        
    load_dotenv() # looks for .env file
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    anthropic = Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key = api_key,
    )

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=make_prompt(prompt_instructions, codebase_txt),
    )
    return completion.completion

def make_prompt(prompt_instructions, codebase_txt):
    return f"{HUMAN_PROMPT} Given the following codebase, answer the question: {prompt_instructions['main_question']} \n {prompt_instructions['guidelines']} \n {codebase_txt} {AI_PROMPT}"

# Questions about the codebase
# 1. Summarize the goal of the codebase.
# 2. What are the main functions in the codebase?
# 3. What are the most important files in the codebase?
# 4. How do the files in the codebase interact with each other?