from typing import Any,List,Dict,Text
from rasa.sdk import Action, Tracker
from rasa.executor import CollectingDispatcher

# class ActionName(Action):
#     def name(self) -> Text:
#         return "action_name"
#
#       #----------------deine all the required custome code here -----------------#
#
#     def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
#         return []
   

class Action_Define(Action):
    def name(self)->Text:
        return "action_define"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]]:
        dispatcher.utter_message("Here's the definition of provident fund")
        return []