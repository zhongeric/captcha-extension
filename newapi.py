from flask import Flask, render_template, request
from threading import Thread
from sys import argv
import logging, time, sys

logging.getLogger('werkzeug').setLevel(logging.ERROR)

token_email_id = {}
tokens = {'tokens':[],'used':[]}

app = Flask(__name__)

def tokenremoval(email_id):
    time.sleep(110)
    token_email_id.pop(email_id)

@app.route('/json', methods=['GET'])
def json():
    content = token_email_id
    return(render_template('json.html', content = content))

@app.route('/solve', methods=['POST'])
def solve():
    if request.method == "POST":
        token = request.form.get('g-recaptcha-response', '')
        email_id = request.form.get('email_id', '')
        token_email_id[email_id] = token
        print('Posted Token : ' + token)
        Thread(target = tokenremoval, args = [email_id]).start()
    return('Success')

@app.route('/', methods=['GET'])
def home():
    return(render_template('main.html'))

# @app.route('/used', methods=['POST'])
# def used():
#     token = request.form.get('usedtoken', '')
#     print('Used Token : ' + token)
#     tokens['used'].append(token)
#     return('Success')

if __name__ == '__main__':
    Thread(target = lambda: app.run(host = '0.0.0.0')).start()
