from flask import Flask, render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# create an instance of the Flask class
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']="postgres://postgres:ninja1pd2ac3@localhost:5432/flask-bick"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class bick(db.Model):
    __tablename__="bicks"

    id=db.Column(db.Integer,primary_key=True)
    brand=db.Column(db.Text)
    db.create_all()
    def __init__(self,id,brand):

        self.id=id
        self.brand = brand


@app.route('/')
def hello():

    return render_template('index.html',bics=bick.query.all())


#creting the CRUD application that will access that by another file
@app.route('/bicks',methods=['GET','POST'])
def index():
    if request.method=='POST':
        bid,b_brand=request.form['model_ID'],request.form['model_name']
        b=bick(id=bid,brand=b_brand)
        db.session.add(b)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html',bics=bick.query.all())

@app.route('/bicks/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        data=bick.query.get(request.form.get('model_ID'))

        data.brand=request.form['model_name']
        db.session.commit()
        return redirect( url_for('index') )

@app.route('/bicks/delete/<int:id>/',methods=['GET',"POST"])
def delete(id):
    data=bick.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('index'))

        #return render_template('show.html',msg="id not found..type correct one")
if __name__=="__main__":
    app.run(debug=True)
