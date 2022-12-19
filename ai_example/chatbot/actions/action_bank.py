from datetime import datetime
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils import format_money

DAILY_GIFT = 100000


class ActionBankBalance(Action):

    def name(self) -> Text:
        return "action_bank_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            balance = tracker.slots.get("balance")
            dispatcher.utter_message(response="utter_bank_balance", balance=format_money(balance))
        except Exception as e:
            print(str(e))
            pass

        return []


class ActionBankDaily(Action):

    def name(self) -> Text:
        return "action_bank_daily"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            now = datetime.now()
            now_str = now.strftime("%d/%m/%Y %H:%M:%S")
            daily_last_update_str = tracker.slots.get("daily_last_update")
            print(daily_last_update_str)
            if daily_last_update_str is not None:
                daily_last_update = datetime.strptime(daily_last_update_str, "%d/%m/%Y %H:%M:%S")
                time_diff = (now - daily_last_update).total_seconds()
                if time_diff < 12 * 60 * 60:
                    time_remain = 12 * 60 * 60 - time_diff
                    hour = int(time_remain // (60 * 60))
                    minute = int((time_remain - hour * 60 * 60) // 60)
                    second = int(time_remain % 60)
                    dispatcher.utter_message(response="utter_bank_daily_2", hour=hour, minute=minute, second=second)
                else:
                    balance = tracker.slots.get("balance")
                    balance = balance + DAILY_GIFT
                    dispatcher.utter_message(response="utter_bank_daily_1", daily=format_money(DAILY_GIFT),
                                             balance=format_money(balance))
                    return [SlotSet('balance', balance), SlotSet('daily_last_update', now_str)]
            else:
                balance = tracker.slots.get("balance")
                balance = balance + DAILY_GIFT
                dispatcher.utter_message(response="utter_bank_daily_1", daily=format_money(DAILY_GIFT),
                                         balance=format_money(balance))
                return [SlotSet('balance', balance), SlotSet('daily_last_update', now_str)]
        except Exception as e:
            print(str(e))
            return []


class ActionBankCuli(Action):

    def name(self) -> Text:
        return "action_bank_culi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            now = datetime.now()
            culi_last_update_str = tracker.slots.get("culi_last_update")
            if culi_last_update_str is not None:
                daily_last_update = datetime.strptime(culi_last_update_str, "%d/%m/%Y %H:%M:%S")
                time_diff = (now - daily_last_update).total_seconds()
                if time_diff < 12 * 60 * 60:
                    time_remain = 12 * 60 * 60 - time_diff
                    hour = int(time_remain // (60 * 60))
                    minute = int((time_remain - hour * 60 * 60) // 60)
                    second = int(time_remain % 60)
                    dispatcher.utter_message(response="utter_bank_culi_3", hour=hour, minute=minute, second=second)
                else:
                    dispatcher.utter_message(response="utter_bank_culi_1")
                    return []
            else:
                dispatcher.utter_message(response="utter_bank_culi_1")
                return []

        except Exception as e:
            print(str(e))
            return []


class ActionBankCuliChoose(Action):

    def name(self) -> Text:
        return "action_bank_culi_choose"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            now = datetime.now()
            now_str = now.strftime("%d/%m/%Y %H:%M:%S")
            culi_last_update_str = tracker.slots.get("culi_last_update")
            if culi_last_update_str is not None:
                daily_last_update = datetime.strptime(culi_last_update_str, "%d/%m/%Y %H:%M:%S")
                time_diff = (now - daily_last_update).total_seconds()
                if time_diff < 12 * 60 * 60:
                    time_remain = 12 * 60 * 60 - time_diff
                    hour = int(time_remain // (60 * 60))
                    minute = int((time_remain - hour * 60 * 60) // 60)
                    second = int(time_remain % 60)
                    dispatcher.utter_message(response="utter_bank_culi_3", hour=hour, minute=minute, second=second)
                else:
                    culi_job = str(next(tracker.get_latest_entity_values("culi_job"), None)).lower()
                    lucky = 0
                    if culi_job == "long biên":
                        lucky = random.randint(10, 50)
                    if culi_job == "trần duy hưng":
                        lucky = random.randint(20, 100)
                    if culi_job == "phố vọng":
                        lucky = random.randint(50, 150)

                    balance = tracker.slots.get("balance")
                    balance = balance + lucky * 10000
                    lucky = format_money(lucky * 10000)

                    dispatcher.utter_message(response="utter_bank_culi_2", culi_job=culi_job, lucky=lucky)
                    return [SlotSet('balance', balance), SlotSet('culi_last_update', now_str)]
            else:
                culi_job = str(next(tracker.get_latest_entity_values("culi_job"), None)).lower()
                lucky = 0
                if culi_job == "long biên":
                    lucky = random.randint(10, 50)
                if culi_job == "trần duy hưng":
                    lucky = random.randint(20, 100)
                if culi_job == "phố vọng":
                    lucky = random.randint(50, 150)

                balance = tracker.slots.get("balance")
                balance = balance + lucky * 10000
                lucky = format_money(lucky * 10000)

                dispatcher.utter_message(response="utter_bank_culi_2", culi_job=culi_job, lucky=lucky)
                return [SlotSet('balance', balance), SlotSet('culi_last_update', now_str)]

        except Exception as e:
            print(str(e))
            return []
