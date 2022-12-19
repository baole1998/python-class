import json
import random


def get_story():
    f = open('actions/data/story.json')
    data = json.load(f)
    story = random.choice(data)
    return story
