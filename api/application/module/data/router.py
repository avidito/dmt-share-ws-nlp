from datetime import datetime, timedelta
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.utils import get_params
from application.database import engine
from .query import get_scraping_result

# Prepare database session
config_dir = "config"
db_params = get_params(dir=config_dir, filename="db_params.json")
get_db = engine.session_factory(**db_params)

##### Endpoint #####
router = APIRouter(
    prefix = "/data"
)

@router.get(
    "/",
    summary = "Get historical data from start_time to end_time (inclusive)")
def get_data(
    start_date: str = "yesterday",
    end_date: str = "yesterday",
    website: str = "all",
    category: str = "all",
    native_category: str = "all",
    db: Session = Depends(get_db)
):
    # Set default value for params
    start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d") if (start_date == "yesterday") else start_date
    end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d") if (end_date == "yesterday") else end_date
    query_params = {
        "start_date": start_date,
        "end_date": end_date,
        "website": website,
        "category": category,
        "native_category": native_category
    }

    # Query data
    data = get_scraping_result(db, query_params)
    rowcount = len(data)
    return {
        "request_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "query_params": query_params,
        "rowcount": rowcount,
        "data": data
    }
