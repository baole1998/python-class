import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils import format_money


class ActionGameBigSmall(Action):

    def name(self) -> Text:
        return "action_game_bigsmall"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            bet = str(next(tracker.get_latest_entity_values("bet"), None)).lower()
            number = int(next(tracker.get_latest_entity_values("number"), None))
            result_1 = random.randint(1, 6)
            result_2 = random.randint(1, 6)
            result_3 = random.randint(1, 6)
            result_str = str(result_1) + "|" + str(result_2) + "|" + str(result_3)
            result_int = result_1 + result_2 + result_3
            balance = tracker.slots.get("balance")
            if bet == "tài":
                if result_int > 10:
                    dispatcher.utter_message(response="utter_game_bigsmall_1", result_str=result_str,
                                             result_total=result_int, result_bet="Tài",
                                             prize=format_money(number*2))
                    balance = balance + number
                else:
                    dispatcher.utter_message(response="utter_game_bigsmall_2", result_str=result_str,
                                             result_total=result_int, result_bet="Xỉu",money=format_money(number))
                    balance = balance - number
            else:
                if result_int > 10:
                    dispatcher.utter_message(response="utter_game_bigsmall_2", result_str=result_str,
                                             result_total=result_int, result_bet="Tài",money=format_money(number))
                    balance = balance - number
                else:
                    dispatcher.utter_message(response="utter_game_bigsmall_1", result_str=result_str,
                                             result_total=result_int, result_bet="Xỉu",
                                             prize=format_money(number*2))
                    balance = balance + number

            return [SlotSet('balance', balance)]
        except Exception as e:
            print(str(e))

        return []
