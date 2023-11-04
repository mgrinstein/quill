
def make_prompt(prompt_elements: dict):
    return f"""
               Given the following codebase,
               answer the question: {prompt_elements['main_question']} \n
               {prompt_elements['guidelines']} \n {prompt_elements['codebase']}
            """
