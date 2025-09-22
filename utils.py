import json

def load_that_shit():
    with open('config.json') as f:
        data = json.load(f)
    return data