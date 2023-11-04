import requests
import sys
import tempfile
import zipfile
import asyncio

from copy import deepcopy

from .call_claude import call_claude
from .read_dir import read_dir
from .langchain_prompt import create_multi_var_prompt
from .mermaid_to_svg import mermaid_to_svg


markdown_template = open("clauding_app/src/template.md", "r").read()
PROMPT_ELEMENTS_README = {
    "main_request": "create a markdown file that summarizes it.",
    "guidelines": "Do not include an introductory text for your answer. Please only output the .MD file directly.",
    "additional_request": f"Build up from the following template, as well as general industry best practices for README files: \n MARKDOWN TEMPLATE START:\n {markdown_template} \n MARKDOWN TEMPLATE END",
}

PROMPT_ELEMENTS_DIAGRAM = {
    "main_request": "create a diagram that summarizes it.",
    "guidelines": "Use the mermaid diagram generator library. Please only respond with a diagram, don't say anything else.",
}

def generate_readme(repo_path, output_file, branch="master"):
    temp_dir = tempfile.mkdtemp()

    if repo_path.startswith("http"):
        repo_path = _download_repo(repo_path, temp_dir, branch)
    print("Reading repo...")
    codebase = read_dir(repo_path)

    prompt_elements_readme = deepcopy(PROMPT_ELEMENTS_README)
    prompt_elements_readme[
        "codebase"
    ] = f"The code base consists of the following files and contents: \n {codebase}"

    prompt_readme = create_multi_var_prompt(prompt_elements_readme)
    print(prompt_readme)

    print("Calling Claude to generate README file...")

    readme_answer = call_claude(prompt_readme)

    if output_file != "":
        with open(output_file, "w") as f:
            f.write(readme_answer)
        print(f"Answer written to {output_file}")
    else:
        print(readme_answer)

    prompt_elements_diagram = deepcopy(PROMPT_ELEMENTS_DIAGRAM)
    prompt_elements_diagram[
        "codebase"
    ] = f"The code base consists of the following files and contents: \n {codebase}"
    prompt_elements_diagram[
        "additional_request"] = f"As reference, you previously said its corresponding README file would look like this: \n {readme_answer}."

    prompt_diagram = create_multi_var_prompt(prompt_elements_diagram)
    print(prompt_diagram)

    print("Calling Claude to generate mermaid diagram...")

    diagram_answer = call_claude(prompt_diagram)
    svg = asyncio.get_event_loop().run_until_complete(mermaid_to_svg(diagram_answer))

    with open("output.svg", "w") as svg_file:
        svg_file.write(svg)
    return readme_answer


def _download_repo(repo_path, temp_dir, branch):
    print("Downloading repo...")
    # Repo is a URL. Download it to a temporary directory
    url = f"{repo_path}/archive/refs/heads/{branch}.zip"
    r = requests.get(url, allow_redirects=True)
    # Unzip the downloaded file
    open(f"{temp_dir}/repo.zip", "wb").write(r.content)
    with zipfile.ZipFile(f"{temp_dir}/repo.zip", "r") as zip_ref:
        zip_ref.extractall(temp_dir)
    return f"{temp_dir}/{repo_path.split('/')[-1]}-{branch}"


if __name__ == "__main__":
    output_file = "test_readme.md"
    generate_readme(sys.argv[1], output_file)
