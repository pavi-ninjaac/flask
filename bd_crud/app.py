from flask import Flask, render_template,request,url_for,redirect
import db_py

# create an instance of the Flask class
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bicks',methods=['GET','POST'])
def show():
    c=db_py.get_all_thinks()
    return render_template('show.html',bick=c)





