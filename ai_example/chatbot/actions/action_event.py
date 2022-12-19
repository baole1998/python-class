from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.api.event import get_event_list

SEARCH_LINK = "https://www.google.com.vn/search?q="


class ActionEvent(Action):

    def name(self) -> Text:
        return "action_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_list = get_event_list()
        event = str(next(tracker.get_latest_entity_values("event"), None)).lower()

        if event == "none":
            dispatcher.utter_message(response="utter_unknown")
        else:
            if event in event_list:
                dispatcher.utter_message(text=event_list[event])
            else:
                link = SEARCH_LINK + event.replace(" ", "+")
                dispatcher.utter_message(response="utter_search", link=link)

        return []
