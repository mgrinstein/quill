import sys

from copy import deepcopy
from call_claude import call_claude
from read_dir import read_dir
from langchain_prompt import create_multi_var_prompt

PROMPT_ELEMENTS = {
    "main_request": "Given the following codebase, create a markdown file that summarizes it.",
    "guidelines": "Do not include an introductory text for your answer. Just output the .MD file directly.",
    "template_to_follow": open("template.md", 'r').read()
}


def main(directory, output_file):
    codebase = read_dir(directory, output_file)

    prompt_elements = deepcopy(PROMPT_ELEMENTS)
    prompt_elements["codebase"] = codebase

    prompt = create_multi_var_prompt(prompt_elements)
    print(prompt)

    answer = call_claude(prompt)
    print(answer)

    if output_file != "":
        with open(output_file, 'w') as f:
            f.write(answer)


if __name__ == '__main__':
    output_file = "test_readme.md"
    main(sys.argv[1], output_file)
