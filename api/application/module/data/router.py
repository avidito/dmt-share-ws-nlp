from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.utils import get_params
from application.database import engine

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
    start_time: str = "today",
    end_time: str = "today",
    category: str = "all",
    native_category: str = "all",
    website: str = "all",
    db: Session = Depends(get_db)
):
    # Set default value for params
    start_time = datetime.now().strftime("%Y-%m-%d") if (start_time == "today") else start_time
    end_time = datetime.now().strftime("%Y-%m-%d") if (end_time == "today") else end_time
    query_params = {
        "start_time": start_time,
        "end_time": end_time,
        "category": category,
        "native_category": native_category,
        "website": website
    }

    # Query data
    # rowcount, data = query.get_scraping_result(db, query_params)
    rowcount, data = None, None
    return {
        "request_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "query_params": query_params,
        "rowcount": rowcount,
        "data": data
    }
