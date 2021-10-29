from datetime import datetime, timedelta
from fastapi import APIRouter

from .classifier import classify_title

##### Endpoint #####
router = APIRouter(
    prefix = "/classify"
)

@router.get("/")
async def classify(
    title: str
):
    result, proba = classify_title(title)
    return {
        "request_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": title,
        "category": result,
        "probability": proba
    }
