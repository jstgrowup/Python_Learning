import json
data={"name":"Alice","age":23}
with open("data.json","w") as f:
    json.dump(data,f)  # Convert dict to JSON and write

with open("data.json","r") as f:
    data=json.load(f) # Read JSON and convert to dict
    print(data["name"])