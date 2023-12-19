
import requests
import time
from flask import Flask, request
import os

TOKEN = os.environ.get('TOKEN')
WEATHER_TOKEN = os.environ.get('WEATHER_TOKEN')
requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook" , json={'url': 'https://flask-tg-bot.onrender.com'})

params = {
  'access_key': WEATHER_TOKEN,
  'query': 'Novosibirsk'
}

app = Flask(__name__)
def send_message(chat_id,text):
    method = "sendMessage"
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    data = {'chat_id':chat_id, 'text':text}
    requests.post(url, data=data)
    
@app.route("/", methods=['GET', 'POST'])
def receive_update():
    if request.method == 'POST':
        #print(request.json)
        chat_id = request.json['message']['chat']['id']
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()
        text = u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature'])
        send_message(chat_id, text)
    return {'ok':True}




