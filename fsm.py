from transitions.extensions import GraphMachine

from utils import send_text_message
from linebot import *
from linebot.models.send_messages import TextSendMessage
from linebot.models.template import ButtonsTemplate, ConfirmTemplate, TemplateSendMessage
from linebot.models.actions import MessageAction, PostbackAction, URIAction

line_bot_api = LineBotApi("nAOGBdhTa49RFIeaNBZzwFidsSGSd75vgCTo9lkhfndEsG2n58/CPw+oxHqqGMaplpxEzLDGhVtl2J9Hv4MLVbO/erT2WdA5pH0//GzukgUAhvAfxLUAFugC6tG2FNIQuOZJMiu9g8SHRid6yV6zKgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("de0f32226af4c2988cfafed82ecd3ff5")   

class player():
    def __init__(self, num):
        self.number = int(num)
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
CurrentPlayer = 0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    def is_going_to_enter_player(self, event):
        text = event.message.text
        return text.lower() == "start"
    def is_going_to_enter_player2(self, event):
        text = event.message.text
        return 1
    def is_going_to_add_player(self, event):
        text = event.message.text
        return text.lower() == "add_player"
    def is_going_to_success_player(self, event):
        text = event.message.text
        player_num.append(player(text))
        return isinstance(text, str) == True
    def is_going_to_enter_number(self, event):
        text = event.message.text
        return text.lower() == "game"
    def is_going_to_statistic(self, event):
        text = event.message.text
        CurrentPlayer = int(text)
        print(text)
        print(CurrentPlayer)
        return isinstance(text, str) == True 
    def is_going_to_twopt(self, event):
        text = event.message.text
        return text.lower() == "twopt"
    def is_going_to_twoptmade(self, event):
        text = event.message.text
        print(CurrentPlayer)
        return text.lower() == "twoptmade"
    def is_going_to_twoptmiss(self, event):
        text = event.message.text
        print(CurrentPlayer)
        return text.lower() == "twoptmiss"
    def gotit(self, event):
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
        send_text_message(reply_token, "Enter anything to next")     
    def on_exit_success_player(self, event):
        print("exit_success_player")

    def on_enter_enter_number(self, event):
        print("Start to choose")
        message = TextSendMessage(text='Enter player number')
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_enter_number(self, event):
        print("exit_enter_number")

    def on_enter_statistic(self, event):
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
                        label='兩分球出手',
                        text='twopt'
                    ),
                    MessageAction(
                        label='三分球出手',
                        text='threept'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)   
    def on_exit_statistic(self, event):
        print("exit_statistic")


    def on_enter_twopt(self, event):
        print("Start to choose")
        #message = TextSendMessage(text='Enter player number')
        #line_bot_api.reply_message(event.reply_token, message)
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='選擇是否命中',
                actions=[
                    MessageAction(
                        label='命中',
                        text='twoptmade'
                    ),
                    MessageAction(
                        label='未命中',
                        text='twoptmiss'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)   
    def on_exit_twopt(self, event):
        print("exit_twopt")

    def on_enter_twoptmade(self, event):
        print("Start to choose") 
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer :
                player_num[i].two_made += 1
                print(player_num[i].two_made)
        message = TextSendMessage(text='Got_it')
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_twoptmade(self, event):
        print("exit_twoptmade")

    def on_enter_twoptmiss(self, event):
        print("Start to choose") 
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer :
                player_num[i].two_miss += 1
        print(player_num[0].number)
        print(CurrentPlayer)
        print(player_num[0].two_miss)
        print(player_num[1].number)
        message = TextSendMessage(text='Got_it')
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_twoptmiss(self, event):
        print("exit_twoptmiss")
    