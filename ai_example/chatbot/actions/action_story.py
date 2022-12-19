from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.api.story import get_story


class ActionStory(Action):

    def name(self) -> Text:
        return "action_story"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        story = get_story()
        dispatcher.utter_message(template="utter_story", story=story)

        return []
