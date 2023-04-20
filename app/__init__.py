from flask import Flask
import re

from flask import Flask, render_template, request, flash, url_for, session, redirect




app = Flask(__name__, template_folder="/templates")



@app.route('/')
def home():
    return render_template('templates\index.html')





if __name__ == '__main__':
    app.run()
