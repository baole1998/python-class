from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.api.people import get_people_list

SEARCH_LINK = "https://www.google.com.vn/search?q="


class ActionPeopleIntro(Action):

    def name(self) -> Text:
        return "action_people_intro"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        people_list = get_people_list()
        people = str(next(tracker.get_latest_entity_values("people"), None)).lower()

        if people == "none":
            dispatcher.utter_message(response="utter_unknown")
        else:
            if people in people_list:
                dispatcher.utter_message(text=people_list[people]["intro"], image=people_list[people]["image"])
            else:
                link = SEARCH_LINK + people.replace(" ", "+")
                dispatcher.utter_message(response="utter_search", link=link)

        return []


class ActionPeopleBirthday(Action):

    def name(self) -> Text:
        return "action_people_birthday"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        people_list = get_people_list()
        people = str(next(tracker.get_latest_entity_values("people"), None)).lower()

        if people == "none":
            dispatcher.utter_message(response="utter_unknown")
        else:
            if people in people_list:
                dispatcher.utter_message(text=people_list[people]["birthday"])
            else:
                link = SEARCH_LINK + people.replace(" ", "+")
                dispatcher.utter_message(response="utter_search", link=link)

        return []


class ActionPeoplePlace(Action):

    def name(self) -> Text:
        return "action_people_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        people_list = get_people_list()
        people = str(next(tracker.get_latest_entity_values("people"), None)).lower()

        if people == "none":
            dispatcher.utter_message(response="utter_unknown")
        else:
            if people in people_list:
                dispatcher.utter_message(text=people_list[people]["place"])
            else:
                link = SEARCH_LINK + people.replace(" ", "+")
                dispatcher.utter_message(response="utter_search", link=link)

        return []
