import sys

from call_claude import call_claude

from read_dir import read_dir

BASE_QUESTION = "Create a markdown file that summarizes the following codebase, skipping the preamble: \n"

def main(directory, output_file):
    codebase_txt = read_dir(directory, output_file)

    answer = call_claude(BASE_QUESTION, codebase_txt)
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
