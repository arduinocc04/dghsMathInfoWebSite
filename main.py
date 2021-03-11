from flask import Flask, render_template, request, redirect, url_for
import base64
app = Flask(__name__)

@app.route('/dghsMathInfo')
def home():
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/constructing')
def constructing():
    return render_template('constructing.html')

@app.route('/recollection')
def recollection():
    #return render_template('recollection.html')
    return redirect(url_for('constructing'))

@app.route('/history')
def history():
    #return render_template('history.html')
    return redirect(url_for('constructing'))

@app.route('/howToEnroll')
def howToEnroll():
    return render_template('howToEnroll.html')

@app.route('/promotion')
def promotion():
    return render_template('promotion.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 80)