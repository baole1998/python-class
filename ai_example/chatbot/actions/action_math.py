from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionMath(Action):

    def name(self) -> Text:
        return "action_math"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = tracker.latest_message.get('text')
        converted_message = self.convert_on_math(text=message)
        print("aloalo", converted_message)
        try:
            if converted_message.split("=")[0] == "":
                dispatcher.utter_message(response="utter_math_ask_result_comparison_1")
                return []

            if "=" in converted_message:
                is_compare, user_result = self.check_number(converted_message.split("=")[1])
                if is_compare:
                    left_operation = self.get_final_operation(converted_message.split("=")[0])
                    result = eval(left_operation)
                    if result == user_result:
                        dispatcher.utter_message(response="utter_math_comparison_1")
                    else:
                        dispatcher.utter_message(response="utter_math_comparison_2", result=result)
                    return []
            result = eval(self.get_final_operation(converted_message))
            dispatcher.utter_message(response="utter_math_1", result=result)
        except:
            dispatcher.utter_message(template="utter_math_2", result=result)

        return []

    def check_number(self, input_string):
        user_result = [int(s) for s in input_string.split() if s.isdigit()]
        if len(user_result) != 0:
            return True, user_result[0]
        return False, None

    def get_final_operation(self, input_string):
        operation = ""
        for i in input_string:
            if i in [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "**", "(", ")",
                     "."]:
                operation += i
        return operation

    def convert_on_math(self, text):
        text = text.lower()
        text = text.replace("bao", "").replace("kh??ng ph???i", ""). \
            replace("kh??ng ????ng", "").replace("????ng kh??ng", "").replace(", ", "")
        text = text.replace("c???ng", "+").replace("tr???", "-") \
            .replace("nh??n", "*").replace("chia", "/") \
            .replace("b???ng", "=").replace("m??", "**") \
            .replace(" ph???y ", ".").replace(",", ".") \
            .replace("^", "**").replace("x", "*") \
            .replace(":", "/")
        text = text.replace("kh??ng", "0").replace("m???t", "1") \
            .replace("hai", "2").replace("ba", "3") \
            .replace("b???n", "4").replace("n??m", "5") \
            .replace("s??u", "6").replace("b???y", "7") \
            .replace("t??m", "8").replace("ch??n", "9") \
            .replace("t??", "4")
        return text
