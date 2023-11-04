import requests
import sys
import tempfile
import zipfile

from copy import deepcopy
from call_claude import call_claude
from read_dir import read_dir
from langchain_prompt import create_multi_var_prompt

PROMPT_ELEMENTS = {
    "main_request": "Given the following codebase, create a markdown file that summarizes it.",
    "guidelines": "Do not include an introductory text for your answer. Just output the .MD file directly.",
    "template_to_follow": open("template.md", 'r').read()
}


def main(repo_path, output_file, branch="master"):
    temp_dir = tempfile.mkdtemp()

    if repo_path.startswith("http"):
        _download_repo(repo_path, temp_dir, branch)
    print("Reading repo...")
    codebase = read_dir(repo_path)

    prompt_elements = deepcopy(PROMPT_ELEMENTS)
    prompt_elements["codebase"] = codebase

    prompt = create_multi_var_prompt(prompt_elements)
    print(prompt)

    print("Calling Claude...")
    answer = call_claude(prompt)

    if output_file != "":
        with open(output_file, 'w') as f:
            f.write(answer)
        print(f"Answer written to {output_file}")
    else:
        print(answer)


def _download_repo(repo_path, temp_dir, branch):
    print("Downloading repo...")
    # Repo is a URL. Download it to a temporary directory
    url = f"{repo_path}/archive/refs/heads/{branch}.zip"
    r = requests.get(url, allow_redirects=True)
    # Unzip the downloaded file
    open(f"{temp_dir}/repo.zip", 'wb').write(r.content)
    with zipfile.ZipFile(f"{temp_dir}/repo.zip", 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    repo_path = f"{temp_dir}/{repo_path.split('/')[-1]}-{branch}"


if __name__ == '__main__':
    output_file = "test_readme.md"
    main(sys.argv[1], output_file)
