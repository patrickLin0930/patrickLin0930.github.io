import requests
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction
from linebot.models import PostbackTemplateAction,URIAction,FlexSendMessage,PostbackEvent,BubbleContainer,BoxComponent,TextComponent  ##new
from linebot.models import (                                                                        ##new-URIA為直接開啟瀏覽器的PACKAGE，剩下的都是跟容器有關(BUBBLE、CAROUSE)，postback是action-class，flex message拿來自定義message的
     MessageAction,FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, URIAction,CarouselContainer,PostbackAction,CarouselColumn,CarouselTemplate
)
from linebot.exceptions import InvalidSignatureError
from flask import request, abort
from flask import Flask
import logging ##new   ##儲存訊息的package


app = Flask(__name__)
##app.logger.setLevel(logging.DEBUG)      ##new  ##儲存錯誤訊息的(有分級別)

line_bot_api = LineBotApi(              #帳號的token
    'WEgKBi2wygDYG9PQv56vqK870sbaGA1Un/J/lYUJ8fP1AQBFSNqtgYYO8hwnl1bgpqZXFwCoorijHdHPl5KUBKUnvPyb8gUO33iDt9xmARkMGnkUZu8i5l8tDFcKY/6qvxJe/Kz8GgZHarn3xpNrfwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d025175f05492f8d604983652a241a99')##Channel secret



##ngrok http 5000                                       

           
ALLOW_HOSTS = ['fbd2-123-205-154-62.ngrok-free.app']        ##new #我的host 

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@使用說明':  # 顯示使用說明 ##目前沒用到這行 先保留
        sendUse(event)     
    #else:  # 一般性輸入
        #sendLUIS(event, mtext)
def sendUse(event):  # 使用說明 ##0目前沒用到
    try:
        text1 = '''選單分成三類,分別是 校園生活/校務資訊/新生專區'''
        message = TextSendMessage(
            text=text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))



if __name__ == '__main__':
    app.run()
