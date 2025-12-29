from pydantic import BaseModel, Field
from typing import Literal


class SummarizeRequest(BaseModel):
    text: str = Field(..., description="The text which need to be summarized")
    summary_type: Literal["short", "bullets", "detailed"] = Field(description="Type of summary which you want to receive from the llm")


class SummarizeResponse(BaseModel):
    summary: str
    usage: dict