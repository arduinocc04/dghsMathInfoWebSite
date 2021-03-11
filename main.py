from flask import Flask, render_template, request, redirect, url_for
import base64
app = Flask(__name__)

@app.route('/dghsMathInfo')
def home():
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/recollection')
def recollection():
    return render_template('recollection.html')

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)