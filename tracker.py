import json
import os

FILE_NAME = "water_data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return {"count": 0}

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(count):
    with open(FILE_NAME, "w") as file:
        json.dump({"count": count}, file)