from fastapi import APIRouter

from datetime import datetime

router = APIRouter(
    prefix = "/log"
)

##### Endpoint #####
@router.get(
    "/",
    summary = "Get model performance logs")
def get_data(
    start_time: str = "today",
    end_time: str = "today",
):
    # Set default value for params
    start_time = datetime.now().strftime("%Y-%m-%d") if (start_time == "today") else start_time
    end_time = datetime.now().strftime("%Y-%m-%d") if (end_time == "today") else end_time
    query_params = {
        "start_time": start_time,
        "end_time": end_time,
    }

    # Query data
    # rowcount, data = query.get_model_logs(db, query_params)
    rowcount, data = None, None
    return {
        "request_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "query_params": query_params,
        "rowcount": rowcount,
        "data": data
    }
