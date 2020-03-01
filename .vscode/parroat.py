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

app = Flask(__name__)

line_bot_api = LineBotApi('tTgnFweD3c7WITielfBBPGQsrRO2Mb31dsbM78q/2t5Zu55L+3KQKS6pGhND/AtdpCueaE69R0EjZv/WHppYlgnFvFOoI64GMeDacS7f8cKb9oWOdjuuXSzlzCbKen3iuePQhpkmgC/Bi1qDGXDz9AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d9129823ae6eb3c5df96de9f46703629')

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host='127.0.0.1')
    #app.run()