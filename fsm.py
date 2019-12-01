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

class Cplayer():
    def __init__(self, num):
        self.number = int(num)  

player_num = []
CurrentPlayer = []

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
        CurrentPlayer.append(Cplayer(text))
        return isinstance(text, str) == True 

    def is_going_to_twopt(self, event):
        text = event.message.text
        return text.lower() == "twopt"
    def is_going_to_twoptmade(self, event):
        text = event.message.text
        return text.lower() == "twoptmade"
    def is_going_to_twoptmiss(self, event):
        text = event.message.text
        return text.lower() == "twoptmiss"

    def is_going_to_threept(self, event):
        text = event.message.text
        return text.lower() == "threept"
    def is_going_to_threeptmade(self, event):
        text = event.message.text
        return text.lower() == "threeptmade"
    def is_going_to_threeptmiss(self, event):
        text = event.message.text
        return text.lower() == "threeptmiss"

    def is_going_to_freept(self, event):
        text = event.message.text
        return text.lower() == "freept"
    def is_going_to_freeptmade(self, event):
        text = event.message.text
        return text.lower() == "freeptmade"
    def is_going_to_freeptmiss(self, event):
        text = event.message.text
        return text.lower() == "freeptmiss"

    def is_going_to_Rebound(self, event):
        text = event.message.text
        return text.lower() == "rebound"
    def is_going_to_ORebound(self, event):
        text = event.message.text
        return text.lower() == "orebound"
    def is_going_to_DRebound(self, event):
        text = event.message.text
        return text.lower() == "drebound"
    
    def gotit(self, event):
        text = event.message.text
        return isinstance(text, str) == True
    def is_going_to_exit(self, event):
        text = event.message.text
        return text.lower() == "exit"


    def on_enter_enter_player(self, event):
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
        message = TextSendMessage(text='Enter player number')
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_enter_number(self, event):
        print("exit_enter_number")

    def on_enter_statistic(self, event):
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
                    MessageAction(
                        label='罰球出手',
                        text='freept'
                    ),
                    MessageAction(
                        label='籃板球',
                        text='rebound'
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)   
    def on_exit_statistic(self, event):
        print("exit_statistic")

    def on_enter_twopt(self, event):
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
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].two_made += 1
                print(player_num[i].two_made)
        print("Number %d made two %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].two_made))
        message = TextSendMessage(text="No.%d made %d 2pt" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].two_made))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_twoptmade(self, event):
        print("exit_twoptmade")

    def on_enter_twoptmiss(self, event):
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].two_miss += 1
        print("Number %d miss two %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].two_miss))
        message = TextSendMessage(text="No.%d miss %d 2pt" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].two_miss))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_twoptmiss(self, event):
        print("exit_twoptmiss")
    
    def on_enter_threept(self, event):
        #message = TextSendMessage(text='Enter player number')
        #line_bot_api.reply_message(event.reply_token, message)
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='選擇是否命中',
                actions=[
                    MessageAction(
                        label='命中',
                        text='threeptmade'
                    ),
                    MessageAction(
                        label='未命中',
                        text='threeptmiss'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)   
    def on_exit_threept(self, event):
        print("exit_threept")

    def on_enter_threeptmade(self, event):
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].three_made += 1
                print(player_num[i].three_made)
        print("Number %d made three %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].three_made))
        message = TextSendMessage(text="No.%d made %d 3pt" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].three_made))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_threeptmade(self, event):
        print("exit_threeptmade")

    def on_enter_threeptmiss(self, event):
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].three_miss += 1
        print("Number %d miss three %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].three_miss))
        message = TextSendMessage(text="No.%d miss %d 3pt" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].three_miss))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_threeptmiss(self, event):
        print("exit_threeptmiss")
    
    def on_enter_freept(self, event):
        #message = TextSendMessage(text='Enter player number')
        #line_bot_api.reply_message(event.reply_token, message)
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='選擇是否命中',
                actions=[
                    MessageAction(
                        label='命中',
                        text='freeptmade'
                    ),
                    MessageAction(
                        label='未命中',
                        text='freeptmiss'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)   
    def on_exit_freept(self, event):
        print("exit_freept")

    def on_enter_freeptmade(self, event):
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].free_made += 1
                print(player_num[i].free_made)
        print("Number %d made one %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].free_made))
        message = TextSendMessage(text="No.%d made %d 1pt" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].free_made))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_freeptmade(self, event):
        print("exit_freeptmade")

    def on_enter_freeptmiss(self, event):
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].free_miss += 1
        print("Number %d miss free %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].free_miss))
        message = TextSendMessage(text="No.%d miss %d 1pt" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].free_miss))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_freeptmiss(self, event):
        print("exit_freeptmiss")

    def on_enter_Rebound(self, event):
        #message = TextSendMessage(text='Enter player number')
        #line_bot_api.reply_message(event.reply_token, message)
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='選擇籃板種類',
                actions=[
                    MessageAction(
                        label='進攻籃板',
                        text='orebound'
                    ),
                    MessageAction(
                        label='防守籃板',
                        text='drebound'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_Rebound(self, event):
        print("exit_Rebound")
    
    def on_enter_ORebound(self, event):
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].ORebound += 1
                print(player_num[i].ORebound)
        print("Number %d made one %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[0].ORebound))
        message = TextSendMessage(text="No.%d made %d OReb" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[CurrentPlayer[len(CurrentPlayer)-1].number].ORebound))
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_ORebound(self, event):
        print("exit_ORebound")

    def on_enter_DRebound(self, event):
        now = 0
        for i in range(len(player_num)) :
            if player_num[i].number == CurrentPlayer[len(CurrentPlayer)-1].number :
                player_num[i].DRebound += 1
                print(player_num[i].DRebound)
                now = i
        print("Number %d made one %d times" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[now].DRebound))
        #message = TextSendMessage(text="No.%d made %d DReb" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[now].DRebound))
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text="No.%d made %d DReb" %(CurrentPlayer[len(CurrentPlayer)-1].number, player_num[now].DRebound),
                actions=[
                    MessageAction(
                        label='check',
                        text='check'
                    ),
                    MessageAction(
                        label='check',
                        text='check'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    def on_exit_DRebound(self, event):
        print("exit_DRebound")