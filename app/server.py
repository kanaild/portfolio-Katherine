from flask import Flask, render_template


site = Flask(__name__)  

#landing page
@site.route('/')
def home():
    return render_template('home-page.html')

#about page
@site.route('/about/')
def about():
    return render_template('about-page.html')

#education page
@site.route('/education/')
def education():
    return render_template('education-page.html')

#work page
@site.route('/work/')
def work():
    return render_template('work-page.html')

#hobbies page
@site.route('/hobbies/')
def hobbies():
    return render_template('hobbies-page.html')

#travel page
@site.route('/travel/')
def travel():
    return render_template('travel-page.html')

if __name__ == '__main__':
    site.run(debug = True)

