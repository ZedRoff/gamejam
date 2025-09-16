
import json

def parse(json_filename):
    json1_file = open(json_filename)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data
