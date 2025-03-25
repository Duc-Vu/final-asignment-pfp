import json
file_path = "database/data.json"
def load_data(file_path=file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        with open(file_path, "w") as f:
            data = {}
            json.dump(data, f, indent= 4)
    return data