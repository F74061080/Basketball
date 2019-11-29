from transitions.extensions import GraphMachine

from utils import send_text_message
from linebot import *
from linebot.models.send_messages import TextSendMessage

line_bot_api = LineBotApi("nAOGBdhTa49RFIeaNBZzwFidsSGSd75vgCTo9lkhfndEsG2n58/CPw+oxHqqGMaplpxEzLDGhVtl2J9Hv4MLVbO/erT2WdA5pH0//GzukgUAhvAfxLUAFugC6tG2FNIQuOZJMiu9g8SHRid6yV6zKgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("de0f32226af4c2988cfafed82ecd3ff5")    

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "go"

    def is_going_to_tainan(self, event):
        text = event.message.text
        return text.lower() == "tainan"

    def is_going_to_taichung(self, event):
        text = event.message.text
        return text.lower() == "taichung"

    def is_going_to_exit(self, event):
        text = event.message.text
        return text.lower() == "exit"

    def on_enter_start(self, event):
        print("Start to choose")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Enter a Country")
        message = TextSendMessage(text='Enter a Country')
        line_bot_api.reply_message(event.reply_token, message)
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


    def on_enter_exit(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Now exit")
        self.go_back()

    def on_exit_exit(self):
        print("Leaving state3")