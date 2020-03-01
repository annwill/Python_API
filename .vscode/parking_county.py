import requests
import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


def getPark(county):
    park_msg=""
    url='http://api.kcg.gov.tw/api/service/get/897e552a-2887-4f6f-a6ee-709f7fbe0ee3'
    r=requests.get(url)
    r.recodin='utf-8'
    js=json.loads(r.text)
    park=js['data'] #抓出所有park的value值

    # dist=input('請輸入查詢的區域 :')
    # print('查詢 {} 臨時停車所'.format(dist))
 
    for item in park:
        if item['行政區']==county:
            park_msg +='地點:'+ item['臨時停車處所'] +'、小型停車位: '+ item['可提供小型車停車位'] +'、地址: '+ item['地址']+'\n'

    if park_msg =='':
        park_msg='查無資料'  
 
    # print( park_msg)
    # print('查詢結束')      
    return park_msg


app = Flask(__name__)

line_bot_api = LineBotApi('')
handler = WebhookHandler('')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=getPark(text))
    )

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run()