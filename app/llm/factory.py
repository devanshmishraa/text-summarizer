from app.llm.mock import MockLLMClient

def get_llm_client():
    # Later: read from env/config
    return MockLLMClient()