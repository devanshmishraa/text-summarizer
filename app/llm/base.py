from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt:str) -> dict:
        """
        Genearate text form a prompt and return text + tokens
        """

        pass