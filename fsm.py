from transitions.extensions import GraphMachine

from utils import send_text_message
from linebot import *

LineBotApi = LineBotApi("nAOGBdhTa49RFIeaNBZzwFidsSGSd75vgCTo9lkhfndEsG2n58/CPw+oxHqqGMaplpxEzLDGhVtl2J9Hv4MLVbO/erT2WdA5pH0//GzukgUAhvAfxLUAFugC6tG2FNIQuOZJMiu9g8SHRid6yV6zKgdB04t89/1O/w1cDnyilFU=")


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        return 1

    def is_going_to_tainan(self, event):
        text = event.message.text
        return text.lower() == "Tainan"

    def is_going_to_taichung(self, event):
        text = event.message.text
        return text.lower() == "Taichung"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "go to state3"

    def on_enter_start(self, event):
        print("Start to choose")

        reply_token = event.reply_token
        send_text_message(reply_token, "Enter a Country")
        #self.go_back()

    def on_exit_start(self, event):
        print("Entering Country")


    def on_enter_tainan(self, event):
        print("I'm entering tainan")

        reply_token = event.reply_token
        send_text_message(reply_token, "Now in tainan")
        #self.go_back()

    def on_exit_tainan(self, event):
        print("Leaving tainan")


    def on_enter_taichung(self, event):
        print("I'm entering taichung")

        reply_token = event.reply_token
        send_text_message(reply_token, "Now in taichung")
        #self.go_back()


    def on_exit_taichung(self,event):
        print("Leaving taichung")


    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
