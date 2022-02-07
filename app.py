from flask import Flask
from flask import request
from telebot import TelegramBot
import os

app = Flask(__name__)

tele_bot = TelegramBot()

@app.route("/")
def root_page():
    return "Dejavu Telegram Client"

@app.route("/api/send", methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        data = request.data
        print(data)
        tele_bot.send(data)
        return data, 200
    elif request.method == 'GET':
        data = request.args.get("data")
        print(data)
        tele_bot.send(data)
        return data, 200

app.run(debug=True, port=5000)
