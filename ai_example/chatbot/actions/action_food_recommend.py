from typing import Any, Text, Dict, List
import random, json

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionFoodRecommend(Action):

    def name(self) -> Text:
        return "action_food_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        used_food = tracker.slots.get("used_food")
        last_food = tracker.slots.get("last_food")
        food_list = self.get_food_list()

        if used_food is None:
            used_food = last_food
        else:
            used_food = used_food + "," + last_food

        if used_food is not None:
            used_food_arr = used_food.split(",")
            for food in used_food_arr:
                if food in food_list:
                    food_list.remove(food)

        if len(food_list) == 0:
            food_list = self.get_food_list()
            used_food = last_food

        dispatcher.utter_message(response="utter_food_recommend", food=random.choice(food_list))

        return [SlotSet("used_food", used_food)]

    def get_food_list(self):
        f = open('actions/data/food.json')
        data = json.load(f)
        return data
