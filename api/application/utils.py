import os
import json

def get_params(dir: str, filename: str):
    filepath = os.path.join(dir, filename)
    with open(filepath, "r") as file:
        tags_metadata = json.load(file)
    return tags_metadata
