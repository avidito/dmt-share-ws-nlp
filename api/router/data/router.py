from fastapi import APIRouter

from datetime import datetime

router = APIRouter(
    prefix = "/data"
)

##### Endpoint #####
@router.get(
    "/",
    summary = "Get historical data from start_time to end_time (inclusive)")
def get_data(
    start_time: str = "today",
    end_time: str = "today",
    category: str = "all",
    native_category: str = "all",
    website: str = "all",
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
