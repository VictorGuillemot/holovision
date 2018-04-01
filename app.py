from flask import Flask, render_template, Response
from datetime import datetime
import tensorflow as tf
#import opencv-python
import numpy as np

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)