from flask import Flask, render_template
import datetime
 
app = Flask(__name__)
@app.route('/')
def index():
    time = datetime.date.today()
    return render_template('index.html', time = time)
