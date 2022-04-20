import json

json_data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_file = open("output.json", "w")
json.dump(json_data, json_file, indent = 4)

json_file.close()