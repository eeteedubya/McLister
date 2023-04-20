from flask import Flask
import re

from flask import Flask, render_template, request, flash, url_for, session, redirect




app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')
    # return "This is the new index page."




if __name__ == '__main__':
    app.run()
