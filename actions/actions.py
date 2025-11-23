

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []


# search Product
class ActionCheckProduct(Action):
    def name(self):
        return "action_check_product"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot("product")
        # Simulate API Hit (replace with real API call)
        dispatcher.utter_message(text=f"I am checking the product '{product}' for you...")
        return []
    

# full order placement
class ActionPlaceOrder(Action):
    def name(self):
        return "action_place_order"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot("product")
        # Simulate Order Placement (replace with real order logic)
        dispatcher.utter_message(text=f"Your order for '{product}' has been placed successfully!")
        return []    

#price check
class ActionCheckProduct(Action):
    def name(self):
        return "action_check_price"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot("product")
        # Simulate API Hit (replace with real API call)
        dispatcher.utter_message(text=f"I am checking the price for you...")
        return []
