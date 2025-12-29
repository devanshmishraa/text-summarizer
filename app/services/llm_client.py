from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text(prompt:str) ->dict:
    """
    Sends a prompt to an LLM providers and returns generatd text
    along with token usage.

    """
    if not client.api_key:
        raise RuntimeError("Open ai api key is not set")
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "user", "content":prompt}
            ]
        )
        return {
            "text": response.choices[0].message.content,
            "usage":{
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens":response.usage.completion_tokens,
                "total_tokens":response.usage.total_tokens
            }
        }

    except Exception as e:
        raise RuntimeError("LLM provider error")  from e