from flask import Flask, render_template
import json
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

f = open('app/data/work.json')
data = json.load(f)
f.close()
work = data.copy()
print(work)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/work')
def work():
    return render_template('work.html', work = data)