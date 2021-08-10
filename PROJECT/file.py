from flask import Flask, request, render_template
import re
import requests
from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__)
def check(language, output):
    url = "https://rapidapi.p.rapidapi.com/translateLanguage/translate"
    payload = "{\"target\":\""+language+"\",\"text\":\""+output+"\",\"type\":\"plain\"\r\n}"
    
    print (payload)
    headers = {
            'content-type': "application/json",
            'x-rapidapi-key': "f12d9357d8msh09c66751a51eb47p183435jsn9f0001da9e26",
            'x-rapidapi-host': "Language-translation.p.rapidapi.com"
            }

    response = requests.request("POST", url, data=payload, headers=headers)
    print (response.text)

    return response.json()['translatedText']

#home page
@app.route('/', methods=['GET','POST']) 
def home():
    return render_template('home.html')

#home page
@app.route('/translator', methods=['GET','POST']) 
def translator ():
    return render_template('translator.html')

#translator page
@app.route('/translate', methods=['POST'])
def translate(): 
    language = request.form['langto'] 
    output = request.form['text'] 
    translated = check (language, output)
    return render_template ('translate.html', text=output, ttext=translated)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
