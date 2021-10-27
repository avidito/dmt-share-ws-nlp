import os
from fastapi import FastAPI

from application.utils import get_params
from application.module import data, classify

# Load config
project_dir = os.path.dirname(os.path.realpath(__file__))
config_dir = os.path.join(project_dir, "config")

tags_metadata = get_params(dir=config_dir, filename="tags_metadata.json")

##### Main #####
app = FastAPI(
    title = "DMT Share - News Title Classification - API",
    description = "API to retrieve historical scraping result and model performance logs",
    version = "0.1",
    openapi_tags = tags_metadata
)
app.include_router(data.router, tags=["Data"])
app.include_router(classify.router, tags=["Classify"])
