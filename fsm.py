from transitions.extensions import GraphMachine

from utils import send_text_message
from linebot import *
from linebot.models.send_messages import TextSendMessage
from linebot.models.template import ButtonsTemplate, TemplateSendMessage
from linebot.models.actions import MessageAction, PostbackAction, URIAction

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
    def is_going_to_tainan_view(self, event):
        text = event.message.text
        return text.lower() == "tainan_view"
    def is_going_to_tainan_food(self, event):
        text = event.message.text
        return text.lower() == "tainan_food"
    def is_going_to_taichung_view(self, event):
        text = event.message.text
        return text.lower() == "taichung_view"
    def is_going_to_taichung_food(self, event):
        text = event.message.text
        return text.lower() == "taichung_food"
    def is_going_to_exit(self, event):
        text = event.message.text
        return text.lower() == "exit"

    def on_enter_start(self, event):
        print("Start to choose")
        #message = TextSendMessage(text='Enter a Country')
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/q2soQy5.jpg',
                title='選擇城市',
                text='Please select',
                actions=[
                    MessageAction(
                        label='Tainan',
                        text='tainan'
                    ),
                    MessageAction(
                        label='Taichung',
                        text='taichung'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        #self.go_back()
    def on_exit_start(self, event):
        print("Entering Country")

    def on_enter_tainan(self, event):
        print("I'm entering tainan")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "Now in tainan")

        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/q2soQy5.jpg',
                title='選擇台南服務',
                text='Please select',
                actions=[
                    MessageAction(
                        label='景點',
                        text='tainan_view'
                    ),
                    MessageAction(
                        label='美食',
                        text='tainan_food'
                    ),
                ]
            )
        )
    
        line_bot_api.reply_message(event.reply_token, message)

        #self.go_back()
    def on_exit_tainan(self, event):
        print("Leaving tainan")

    def on_enter_taichung(self, event):
        print("I'm entering taichung")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "Now in taichung")

        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/q2soQy5.jpg',
                title='選擇台中服務',
                text='Please select',
                actions=[
                    MessageAction(
                        label='景點',
                        text='taichung_view'
                    ),
                    MessageAction(
                        label='美食',
                        text='taichung_food'
                    ),
                ]
            )
        )
    
        line_bot_api.reply_message(event.reply_token, message)

        #self.go_back()
    def on_exit_taichung(self,event):
        print("Leaving taichung")

    def on_enter_tainan_food(self, event):
        print("I'm entering tainan")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "Now in tainan")

        message = TextSendMessage(text='It is delicious in Tainan!!')
        line_bot_api.reply_message(event.reply_token, message)

        #self.go_back()
    def on_exit_tainan_food(self, event):
        print("Leaving tainan")

    def on_enter_tainan_view(self, event):
        print("I'm entering tainan")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "Now in tainan")

        message = TextSendMessage(text='It is fun in Tainan!!')
        line_bot_api.reply_message(event.reply_token, message)

        #self.go_back()
    def on_exit_tainan_view(self, event):
        print("Leaving tainan")

    def on_enter_taichung_food(self, event):
        print("I'm entering taichung")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "Now in tainan")

        message = TextSendMessage(text='It is delicious in taichung!!')
        line_bot_api.reply_message(event.reply_token, message)

        #self.go_back()
    def on_exit_taichung_food(self, event):
        print("Leaving taichung")

    def on_enter_taichung_view(self, event):
        print("I'm entering taichung")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "Now in tainan")

        message = TextSendMessage(text='It is fun in taichung!!')
        line_bot_api.reply_message(event.reply_token, message)

        #self.go_back()
    def on_exit_taichung_view(self, event):
        print("Leaving taichung")

    def on_enter_exit(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Now exit")
        self.go_back()
    def on_exit_exit(self):
        print("Leaving state3")