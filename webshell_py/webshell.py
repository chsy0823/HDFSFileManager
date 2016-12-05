import subprocess

import fcntl
import os

import asyncio
from flask import Flask
from flask import json
from flask import render_template
from flask import session
from flask import request

SH_FILE_RECOG = "/usr/share/nginx/html/webshell/classify.sh"
SH_FILE_DEMO = "/usr/share/nginx/html/webshell/classify.sh"
SH_FILE_LEARN = "/usr/share/nginx/html/webshell/classify.sh"
Flask.secret_key = "test123123"
app = Flask(__name__)


proc = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/recognize")
def recognizeView():
    return render_template('index.html')

@app.route("/learning")
def learningView():
    return render_template('index2.html')

@app.route('/execute', methods=['POST'])
def executeCommand():
    # session['output'] = []

    cmd = request.form["command"]
    line = ""

    if cmd == "classify" :
        line = SH_FILE_RECOG
        p = subprocess.Popen(['bash', line], stdout=subprocess.PIPE)
    elif cmd == "learning":
        line = SH_FILE_LEARN
        p = subprocess.Popen(['bash', line], stdout=subprocess.PIPE)
    elif cmd == "demo":
        line = SH_FILE_DEMO
        p = subprocess.Popen(['bash', line], stdout=subprocess.PIPE)
    elif cmd == "showGPU" :
        line = "nvidia-smi"
        p = subprocess.Popen(['nvidia-smi'], stdout=subprocess.PIPE)
    
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

