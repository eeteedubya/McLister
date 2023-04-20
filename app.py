
import re
import os

from flask import Flask, render_template, request, flash, url_for, session, redirect
# import psycopg2
# import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
import json
import jinja2


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    print("looking for template")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
