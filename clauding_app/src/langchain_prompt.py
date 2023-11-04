from langchain.prompts import PromptTemplate

def create_multi_var_prompt(prompt_elements: dict):
    multi_var_prompt = PromptTemplate(
        input_variables=["main_request", "guidelines",
                        "additional_request", "codebase"],
        template="""
                MAIN REQUEST: Given the following codebase, {main_request} \n
                GUIDELINES: {guidelines} \n
                {additional_request} \n
                {codebase} \n
            """
    )

    # Pass in values to the input variables
    prompt = multi_var_prompt.format(
        main_request=prompt_elements['main_request'],
        guidelines=prompt_elements['guidelines'],
        additional_request=prompt_elements['additional_request'],
        codebase=prompt_elements['codebase']
    )

    return prompt
