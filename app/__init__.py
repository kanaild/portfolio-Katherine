from flask import Flask, render_template
import json
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

a = open('app/data/work.json')
work_data = json.load(a)
a.close()
work_d = work_data.copy()

b = open('app/data/hobbies.json')
hobby_data = json.load(b)
b.close()
hobbies_d = hobby_data.copy()

c = open('app/data/education.json')
education_data = json.load(c)
c.close()
education_d = education_data.copy()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/work')
def work():
    return render_template('work.html', work = work_d)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies = hobbies_d)

@app.route('/education')
def education():
    return render_template('education.html', education = education_d)