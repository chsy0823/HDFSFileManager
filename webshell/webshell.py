import subprocess

import fcntl

import asyncio
from flask import Flask
from flask import json
from flask import render_template
from flask import session

SH_FILE_RECOG = "/usr/share/nginx/html/webshell/classify.sh"
SH_FILE_DEMO = "/usr/share/nginx/html/webshell/classify.sh"
SH_FILE_LEARN = "/usr/share/nginx/html/webshell/classify.sh"
Flask.secret_key = "test123123"
app = Flask(__name__)


proc = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    # session['output'] = []
    SH_FILE = SH_FILE_RECOG
	p = subprocess.Popen(['bash', SH_FILE], stdout=subprocess.PIPE)
    global proc
    proc = p

    return "start"


@app.route('/stop', methods=['POST'])
def stop():
    global proc
    proc.terminate()

    return "stop"


@app.route('/tail', methods=['POST'])
def tail():
    global proc
    p = proc

    line = p.stdout.readline()
    return line.decode('utf-8') if len(line) != 0 else ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)

