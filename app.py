from flask import Flask, request, abort, render_template
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import random

app = Flask(__name__)

line_bot_api = LineBotApi('6Y2XVMJ+InBmLLFOpjT/XNhatRXeunl8AplylcGAiQ4hjmIQ7JtsKOfJ/yD1m8F69CxGFdh+1TEOYMlbEsWL5Niq+s2RRjDcHA8Co+Mz06zdG9+ZqOI3kV9UYyL+VnirLcAvR/Y3As1qzcVIeVyoRwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e9514b8093263b97181e52a614fcc329')


@app.route('/callback', methods=['POST'])
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
    reply_message = ""
    if event.message.text == "안녕":
        reply_message = "냥냥"
    elif event.message.text == "귀여워":
        reply_message = "냥냥펀치!"
    elif event.message.text == "심심해":
        reply_message = "우냐앙?😻"
    elif event.message.text == "좋아해":
        reply_message = "후후후😻"
    elif "츄르" in event.message.text:
        reply_message = "뭘 하면 줄꺼냥!"
    elif "날씨" in event.message.text:
        reply_message = "어때?"
    elif event.message.text == "가위" or event.message.text == "바위" or event.message.text == "보":
        reply_list = ["가위", "바위", "보"]
        reply_message = str(random.sample(reply_list, 1)[0])
    else:
        return

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))


if __name__ == '__main__':
    app.run()