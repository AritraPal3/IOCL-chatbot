from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List


# class ActionName(Action):
#     def name(self) -> Text:
#         return "action_name"
#
#       #----------------deine all the required custome code here -----------------#
#
#     def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
#         return []
   

class Action_Documents(Action):
    def name(self)->Text:
        return "action_documents_required"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        dispatcher.utter_message(text="The following are the required documents")
        return []
    
class Action_Benifits(Action):
    def name(self) -> Text:
        return "action_pf_benifit"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        dispatcher.utter_message(text="Here are the benifits of having provident fund")
        return []
    
class Action_Ask(Action):
    def name(self) -> Text:
        return "action_ask"
    
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        dispatcher.utter_message(text="What do you want to know about provident fund")
        return []

class Action_Define(Action):
    def name(self) -> Text:
        return "action_define"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        fund_type=tracker.get_slot('provident fund')
        
        dispatcher.utter_message(text="Here's your definition about "+str(fund_type))
        return []

class Action_Ask_More(Action):
    def name(self) -> Text:
        return "action_ask_more"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        dispatcher.utter_message(text="If you want to know more please let me know")
        return []
    
class Action_Fallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        dispatcher.utter_message(template="utter_fallback")
        return []