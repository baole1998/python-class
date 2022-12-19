import json


def get_today_list():
    f = open('actions/data/today.json')
    data = json.load(f)
    return data