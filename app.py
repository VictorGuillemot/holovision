from flask import Flask, render_template, Response
from datetime import datetime
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)