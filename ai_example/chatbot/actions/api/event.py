import json


def get_event_list():
    f = open('actions/data/event.json')
    data = json.load(f)
    return data
