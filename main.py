import sys

from copy import deepcopy
from call_claude import call_claude
from make_prompt import make_prompt
from read_dir import read_dir

BASE_QUESTION = "Create a markdown file that summarizes the following codebase, skipping the preamble: \n"
GUIDELINES = "Do not include an introductory text for your answer. Just output the .MD file directly \n"

PROMPT_INSTRUCTIONS = {
    "main_question": BASE_QUESTION,
    "guidelines": GUIDELINES
}


def main(directory, output_file):
    codebase = read_dir(directory, output_file)

    prompt = deepcopy(PROMPT_INSTRUCTIONS)
    prompt["codebase"] = codebase

    answer = call_claude(prompt)
    print(answer)

    if output_file != "":
        with open(output_file, 'w') as f:
            f.write(answer)


if __name__ == '__main__':
    output_file = "test_readme.md"
    main(sys.argv[1], output_file)

# Base question:
# Generate a markdown file that summarizes the follwing codebase.
# It contains the following sections:
# Introduction
# 
