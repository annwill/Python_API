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

def getWeather(conty) :
    user_key = "CWB-103F2429-9F63-4410-8393-89512BDCEDB8"
    doc_name = "F-C0032-001"

    api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s&format=JSON" % (doc_name,user_key)
    r = requests.get(api_link)
    dataload = json.loads(r.text)

    index = -1
    tlist = ['天氣狀況', '最高溫', '最低溫', '舒適度', '降雨機率']
    datas = dataload['cwbopendata']['dataset']['location']
    for i in range(len(datas)):
        if datas[i]['locationName'] == conty.replace('台','臺'):
            index = i
            break
    answer = ''
    if index != -1:
        answer = datas[index]['locationName']
        for j in range(5):
            answer += '\n' + tlist[j] + ':' + datas[index]['weatherElement'][j]['time'][0]['parameter']['parameterName']
    else:
        answer = '沒有相關縣市資料！'
    
    return answer

app = Flask(__name__)

line_bot_api = LineBotApi('Channel access token')
handler = WebhookHandler('Channel secret')


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
        TextSendMessage(text=getWeather(text))
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')