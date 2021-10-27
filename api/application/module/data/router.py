from datetime import datetime, timedelta
from fastapi import APIRouter

from .query import get_scraping_result

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
    native_category: str = "all"
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
    data = [row for row in get_scraping_result(query_params)]
    rowcount = len(data)
    return {
        "request_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "query_params": query_params,
        "rowcount": rowcount,
        "data": data
    }
