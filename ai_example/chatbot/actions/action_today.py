from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.api.today import get_today_list
from datetime import datetime
class ActionToDay(Action):

    def name(self) -> Text:
        return "action_today"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        day=datetime.today().strftime('%d-%m')
        list_day = []
        for key in get_today_list().keys():
            list_day.append(key)
        if day in list_day:
            print(day)
            event = "\n".join(get_today_list()[day]["Sự kiện"])
            born = "\n".join(get_today_list()[day]["Sinh"])
            dead = "\n".join(get_today_list()[day]["Mất"])
            dispatcher.utter_message(template="utter_today", event=event,born=born,dead=dead )
        else:
            dispatcher.utter_message(template="utter_today_none")
