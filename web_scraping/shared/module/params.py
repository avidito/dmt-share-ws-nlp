import sys
import json
from datetime import datetime, timedelta

# Get arguments from runtime
def get_args(params_count):
    params = sys.argv[1:]
    missing = params_count - len(params)
    params = params + [None] * missing
    return params

# Get config JSON file
def get_config_json(path):
    with open(path, "r", encoding="utf-8") as file:
        raw_json = "\n".join(file.readlines())
    return json.loads(raw_json)

# Generate date path/query params
def get_date_params(date, time_format, type):
    date_str = date.strftime(time_format)

    if (type == "path"):
        return {"path": date_str}
    elif (type == "query"):
        return {"query": {"date": date_str}}
