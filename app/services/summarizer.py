
from app.services.prompt_builder import prompt_formatter
from app.services.llm_client import generate_text
def summary(text_to_summarize:str, type_of_summary:str) -> dict:
    """Coordinates summarization by building prompt and invoking LLM client
        Independent of web frameworks and LLM provider"""
    
    """
    Orchestrates the summarization workflow by:
    1.Building the prompt
    2.Invoking the LLM client
    """

    if not text_to_summarize or not text_to_summarize.strip():
        raise ValueError("Text to summarize can not be empty")

    prompt = prompt_formatter(text_to_summarize, type_of_summary)

    llm_response = generate_text(prompt)


    return {
        "summary":llm_response["text"],
        "usage": llm_response["usage"]
    }

summary("hey there", "bullets")