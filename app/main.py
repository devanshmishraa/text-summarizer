from fastapi import FastAPI
from app.api.routes.summarize import router as summarize_router


app = FastAPI(title = "LLM Summarization Service")

app.include_router(summarize_router, prefix = "/api")