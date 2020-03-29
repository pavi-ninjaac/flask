from flask import Flask, render_template,request,url_for,redirect
from index import bick

# create an instance of the Flask class
app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    return render_template('base.html')


#creting the CRUD application that will access that by another file
honda=bick(brand='honda')
ktm=bick(brand='ktm')
apache=bick(brand='apache')
ninja=bick(brand='ninja')
bicks_list=[honda,ktm,apache,ninja]
@app.route('/bicks',methods=['GET','POST'])
def index():
    if request.method=='POST':
        bi=request.form['new_bick']
        bicks_list.append(bick(bi))
        return redirect(url_for('index'))

    return render_template('index.html',bics=bicks_list)

@app.route('/bicks/new',methods=['post','get'])
def new():
    return render_template('new.html')

@app.route('/bicks/show', methods=['GET','POST'])
def show():
    id=request.form['bick_id']
    found=[ bick for bick in bicks_list if bick.id==id ]
    found_bick=found[0].brand
    return render_template('show.html',msg="your bick name pretty good one",bick=found_bick)
        #return render_template('show.html',msg="id not found..type correct one")
