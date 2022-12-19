import json


def get_people_list():
    f = open('actions/data/people.json')
    data = json.load(f)
    return data
