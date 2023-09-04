from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
import random

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
        dispatcher.utter_message(response="utter_default")
        return []
    
class Action_Explain(Action):
    def name(self)->Text:
        return "action_ans_explain"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any])->List[Dict[Text,Any]]:
        anscontainer=[
            "A provident fund is a financial savings scheme designed to help individuals save money for their retirement.",
            "A provident fund is a long-term savings account that aims to provide financial security to individuals after they retire from work.",
            "A provident fund, often abbreviated as 'PF' is a retirement-oriented investment fund where employees and employers contribute a portion of the employee's salary regularly.",
            "A provident fund is a tax-advantaged retirement savings plan that enables employees to set aside a portion of their income for their future retirement needs.",
            "A provident fund is a type of investment fund established by employers to assist employees in building a financial cushion for retirement.",
            "A provident fund is a retirement savings scheme that offers employees a disciplined way to accumulate funds for their post-retirement life.",
            "Provident funds are investment vehicles that help individuals save money over their working years, with the aim of providing financial support during retirement.",
            "A provident fund is a financial instrument that encourages long-term savings and investments to ensure financial stability during one's retirement years.",
            "Provident funds are structured savings plans that facilitate systematic retirement planning by both employees and employers.",
            "A provident fund is a retirement benefit scheme that offers financial protection to employees in their post-retirement years.",
        ]
        answer=random.choice(anscontainer)
        dispatcher.utter_message(text=answer)
        return []