from transitions.extensions import GraphMachine

from utils import send_text_message
from linebot import *
from linebot.models.send_messages import TextSendMessage
from linebot.models.template import ButtonsTemplate, TemplateSendMessage
from linebot.models.actions import MessageAction, PostbackAction, URIAction

line_bot_api = LineBotApi("nAOGBdhTa49RFIeaNBZzwFidsSGSd75vgCTo9lkhfndEsG2n58/CPw+oxHqqGMaplpxEzLDGhVtl2J9Hv4MLVbO/erT2WdA5pH0//GzukgUAhvAfxLUAFugC6tG2FNIQuOZJMiu9g8SHRid6yV6zKgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("de0f32226af4c2988cfafed82ecd3ff5")   

class player():
    def __init__(self, num):
        self.number = num
        self.two_made   = 0
        self.two_miss   = 0
        self.three_made = 0
        self.three_miss = 0
        self.free_made  = 0
        self.free_miss  = 0
        self.ORebound   = 0
        self.DRebound   = 0
        self.assist     = 0
        self.steal      = 0
        self.block      = 0
        self.error      = 0
        self.foul       = 0

player_num = []

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_enter_player(self, event):
        text = event.message.text
        return text.lower() == "start"
    def is_going_to_add_player(self, event):
        text = event.message.text
        return text.lower() == "add_player"
    def is_going_to_success_player(self, event):
        text = event.message.text
        return isinstance(text, str) == True
    def is_going_to_exit(self, event):
        text = event.message.text
        return text.lower() == "exit"

    def on_enter_enter_player(self, event):
        print("Start to choose")
        #message = TextSendMessage(text='Enter player number')
        #line_bot_api.reply_message(event.reply_token, message)
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='安安你好',
                text='Please select',
                actions=[
                    MessageAction(
                        label='增加球員',
                        text='add_player'
                    ),
                    MessageAction(
                        label='開始比賽',
                        text='game'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)   
    def on_exit_enter_player(self, event):
        print("exit_enter_player")

    def on_enter_add_player(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter player number")
        
        
    def on_exit_add_player(self, event):
        print("exit_add_player")

    def on_enter_success_player(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Success add player")
        self.go_back()
        
    def on_exit_success_player(self):
        print("exit_success_player")

    def on_enter_exit(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "Now exit")
        self.go_back()
    def on_exit_exit(self):
        print("Leaving state3")