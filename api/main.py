from fastapi import FastAPI

from utils import get_tags_metadata
from router import data, log

app = FastAPI(
    title = "DMT Share - News Title Classification - API",
    description = "API to retrieve historical scraping result and model performance logs",
    version = "0.1",
    openapi_tags = get_tags_metadata()
)
app.include_router(data.router, tags=["Data"])
app.include_router(log.router, tags=["Log"])
