from fastapi import APIRouter, HTTPException
from app.services.summarizer import summary
from app.schemas.summary import SummarizeRequest, SummarizeResponse

router = APIRouter()

@router.post("/summarize", response_model = SummarizeResponse)
def summarize_text(request: SummarizeRequest):
    
    try:
        result = summary(
        text_to_summarize=request.text,
        type_of_summary=request.summary_type
    )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return SummarizeResponse(**result)