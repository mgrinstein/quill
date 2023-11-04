import requests
import sys
import tempfile
import zipfile

from copy import deepcopy
from call_claude import call_claude
from make_prompt import make_prompt
from read_dir import read_dir

TEMP_DIR = "temp"

BASE_QUESTION = "Create a markdown file that summarizes the following codebase, skipping the preamble: \n"
GUIDELINES = "Do not include an introductory text for your answer. Just output the .MD file directly \n"

PROMPT_INSTRUCTIONS = {
    "main_question": BASE_QUESTION,
    "guidelines": GUIDELINES,
    "template": open("template.md", 'r').read()
}


def main(repo_path, output_file, branch="master"):
    temp_dir = tempfile.mkdtemp()

    if repo_path.startswith("http"):
        print("Downloading repo...")
        # Repo is a URL. Download it to a temporary directory
        url = f"{repo_path}/archive/refs/heads/{branch}.zip"
        r = requests.get(url, allow_redirects=True)
        # Unzip the downloaded file
        open(f"{temp_dir}/repo.zip", 'wb').write(r.content)
        with zipfile.ZipFile(f"{temp_dir}/repo.zip", 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        repo_path = f"{temp_dir}/{repo_path.split('/')[-1]}-{branch}"

    print("Reading repo...")
    codebase = read_dir(repo_path)

    prompt = deepcopy(PROMPT_INSTRUCTIONS)
    prompt["codebase"] = codebase

    print("Calling Claude...")
    prompt = make_prompt(prompt)
    answer = call_claude(prompt)

    if output_file != "":
        with open(output_file, 'w') as f:
            f.write(answer)
        print(f"Answer written to {output_file}")
    else:
        print(answer)


if __name__ == '__main__':
    output_file = "test_readme.md"
    main(sys.argv[1], output_file)

