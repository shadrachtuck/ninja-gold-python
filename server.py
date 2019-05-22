from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="shh"
# app.count = 0
import random
@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    izf request.form['building'] == 'casino':
        session['count']+=random.randint(-50,50)
    elif request.form['building'] == 'reset':
        session['count']=0
    elif request.form['building']:
        session['count']+=random.randint(0,100)
    print(session)
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)
