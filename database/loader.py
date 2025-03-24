import json
file_path = "data.json"
def load_file(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        with open(file_path, "w") as f:
            data = {}
            json.dump(data, f, indent= 4)
    return data