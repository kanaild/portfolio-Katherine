from flask import Flask, render_template


site = Flask(__name__)  
@site.route('/')
def home():
    return render_template('home-page.html')


if __name__ == '__main__':
    site.run()

