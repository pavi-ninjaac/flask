from flask import Flask,render_template,request
from detect_text import Detect_text
upload_folder=r'C:\Users\ninjaac\Desktop\images'
app=Flask(__name__)

@app.route('/')
def upload_image_html():
    return render_template('upload_image.html')
@app.route('/detect_image',methods=['GET','POST'])
def upload():
    if request=='POST':
        if file not in request.files:
            return render_template('display_image.html',msg='No file selected')
        file=request.files['file']
        name=request.files['file'].filename
        if file:
            estracted_text=Detect_text(file)
            return render_template('display_image.html',msg='file succesfully submitted',text=estracted_text,img_src=upload_folder+name)

