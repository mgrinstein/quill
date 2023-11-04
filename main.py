import sys

from anthropic import HUMAN_PROMPT, AI_PROMPT

from claude import call_claude
from read_dir import read_dir

PROMPT_START = "{HUMAN_PROMPT} Resume the following repository: \n"
PROMPT_END = "{AI_PROMPT}"
OUTPUT_FILE = "temp.txt"

def main(dir_path):
    read_dir(".", OUTPUT_FILE)
    with open(OUTPUT_FILE, 'r') as f:
        prompt = PROMPT_START + f.read() + PROMPT_END

    print(call_claude(prompt))


if __name__ == "__main__":
    main(sys.argv[1])
