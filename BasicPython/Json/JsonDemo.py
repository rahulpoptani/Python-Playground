import json, os

# JSON to String
json_obj = {"name": "John", "age": 30, "city": "New York"}
json_str = json.dumps(json_obj)
print(json_str)

# String to JSON
json_obj = json.loads(json_str)
print(json_obj)

cwd = os.path.realpath(__file__).replace(os.path.basename(__file__), "")
# JSON to File
with open(f"{cwd}data.json", "w") as file:
    json.dump(json_obj, file)

# File to JSON
with open(f"{cwd}data.json", "r") as file:
    json_obj = json.load(file)
    print(json_obj)

