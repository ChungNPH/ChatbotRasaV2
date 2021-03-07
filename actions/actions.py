# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet, EventType,
)

from rasa_sdk.forms import FormValidationAction, FormAction


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionCheckIDAvaiable(Action):
    def name(self) -> Text:
        return "action_kiem_tra_chung_minh_thu"

    def get_avaiable_id(self, text):
        return text in ['123456789']

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        chung_minh_thu = tracker.get_slot("chung_minh_thu")
        da_co_tai_khoan = self.get_avaiable_id(chung_minh_thu)
        if da_co_tai_khoan:
            dispatcher.utter_message(template="utter_thong_bao_da_co_tai_khoan")
        else:
            dispatcher.utter_message(template="utter_hoi_ekyc")
        return [SlotSet("da_co_tai_khoan", da_co_tai_khoan)]


class ValidateTaiKhoanForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_tai_khoan_form"

    def validate_loai_tai_khoan(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if value.lower() in ["cá nhân", "tổ chức"]:
            return {"loai_tai_khoan": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_loai_tai_khoan")
            return {"loai_tai_khoan": None}

    def validate_chung_minh_thu(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if value.isdigit() and len(value) in [9, 12]:
            return {"chung_minh_thu": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_chung_minh_thu")
            return {"chung_minh_thu": None}


class ActionCheckPIN(Action):
    def name(self) -> Text:
        return "action_kiem_tra_ma_pin"

    def get_avaiable_id(self, text):
        return text in ['@123']

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        ma_pin = tracker.latest_message.get('text')
        print(ma_pin)
        kiem_tra_ma_pin = self.get_avaiable_id(ma_pin)
        if kiem_tra_ma_pin:
            dispatcher.utter_message(template="utter_reset_ma_pin_thanh_cong")
        else:
            dispatcher.utter_message(template="utter_reset_ma_pin_that_bai")
        return [SlotSet("kiem_tra_ma_pin", kiem_tra_ma_pin)]


class ValidateResetPinForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_reset_pin_form"

    def validate_so_tai_khoan(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if (value.lower().startswith('026c') and len(value) == 10 and value[4:].isdigit()) \
                or (value.isdigit() and len(value) == 6):
            return {"so_tai_khoan": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_so_tai_khoan")
            return {"so_tai_khoan": None}

    def valiate_so_dien_thoai(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if value.isdigit():
            return {"so_dien_thoai": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_so_dien_thoai")
            return {"so_dien_thoai": None}


class ValidateUngTienForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_ung_tien_form"

    def validate_so_tai_khoan(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if (value.lower().startswith('026c') and len(value) == 10 and value[4:].isdigit()) \
                or (value.isdigit() and len(value) == 6):
            return {"so_tai_khoan": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_so_tai_khoan")
            return {"so_tai_khoan": None}

    def validate_loai_tai_khoan(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if value.lower() in ["cá nhân", "tổ chức"]:
            return {"loai_tai_khoan": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_loai_tai_khoan")
            return {"loai_tai_khoan": None}

    def validate_chung_minh_thu(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if value.isdigit() and len(value) in [9, 12]:
            return {"chung_minh_thu": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_chung_minh_thu")
            return {"chung_minh_thu": None}

    def validate_tieu_khoan(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if value.isdigit() and value in ['1', '3', '6']:
            return {"tieu_khoan": value}
        else:
            dispatcher.utter_message(template="utter_not_validate_tieu_khoan")
            return {"tieu_khoan": None}