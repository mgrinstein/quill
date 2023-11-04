from langchain.prompts import PromptTemplate
from anthropic import HUMAN_PROMPT, AI_PROMPT


def create_multi_var_prompt(prompt_elements: dict):
    multi_var_prompt = PromptTemplate(
        input_variables=["main_request", "guidelines", "diagram",
                        "template_to_follow", "codebase"],
        template="""
                {HUMAN_PROMPT}
                {main_request} \n
                {guidelines} \n
                {diagram} \n
                {template_to_follow} \n
                {codebase} \n
                {AI_PROMPT}
            """
    )

    # Pass in values to the input variables
    prompt = multi_var_prompt.format(
        human_prompt=HUMAN_PROMPT,
        main_request=prompt_elements['main_request'],
        guidelines=prompt_elements['guidelines'],
        template_to_follow=prompt_elements['template_to_follow'],
        diagram=prompt_elements['diagram'],
        codebase=prompt_elements['codebase'],
        ai_prompt=AI_PROMPT
    )

    return prompt
