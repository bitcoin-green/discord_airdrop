import json
import os

def jsonfile(filename, data):
    try:
        with open(filename, 'w') as f:
            decode_jdata = json.dumps(json.JSONDecoder().decode(data))
            reload = json.loads(decode_jdata)
            json.dump(reload, f, indent=4)
    except Exception as e:
        print (e)

def load_json(path):
    if os.path.isfile(path):
        with open(path) as f:
            return json.load(f)

def parse2json(data):
    return json.dumps(data, indent=4)

def check_duplicate(item, list):
    if item in list:
        return True
    else:
        return False