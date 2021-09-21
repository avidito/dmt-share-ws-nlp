import os
import json

def get_tags_metadata(dir: str = "config"):
    """
    Get tags metadata configuration from config file.
    """

    filepath = os.path.join(dir, "tags_metadata.json")
    with open(filepath, "r") as file:
        tags_metadata = json.load(file)
    return tags_metadata
