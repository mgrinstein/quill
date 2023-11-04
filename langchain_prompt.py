from langchain.prompts import PromptTemplate


def create_multi_var_prompt(prompt_elements: dict):
    multi_var_prompt = PromptTemplate(
        input_variables=["main_request", "guidelines",
                        "template_to_follow", "codebase"],
        template="""
                {main_request} \n
                {guidelines} \n
                Build up from the following template, as well as general industry best practices for README files: {template_to_follow} \n
                The code base consists of the following files and contents: {codebase} \n
            """
    )

    # Pass in values to the input variables
    prompt = multi_var_prompt.format(
        main_request=prompt_elements['main_request'],
        guidelines=prompt_elements['guidelines'],
        template_to_follow=prompt_elements['template_to_follow'],
        codebase=prompt_elements['codebase']
    )

    return prompt
