

def prompt_formatter(text_to_summarize:str, type_of_summary:str) -> str:
    summary_types = {
        "short": "short and concise single paragraph",
        "bullets": "concise bullet points no paragraph text",
        "detailed": "detailed may be more than one paragraph"
    }

    final_prompt = f"""summarize the following text in {summary_types[type_of_summary]}\n
                        {text_to_summarize}"""

    return final_prompt