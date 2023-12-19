#!/usr/bin/env python
import requests
import time
from flask import Flask, request



TOKEN = mySecrets.TOKEN



requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook" , json={'url': 'https://flask-tg-bot.onrender.com'})


app = Flask(__name__)
def send_message(chat_id,text):
    method = "sendMessage"
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    data = {'chat_id':chat_id, 'text':text}
    requests.post(url, data=data)
    
@app.route("/", methods=['GET', 'POST'])
def receive_update():
    if request.method == 'POST':
        print(request.json)
        chat_id = request.json['message']['chat']['id']
        send_message(chat_id, 'pong')
    return {'ok':True}




