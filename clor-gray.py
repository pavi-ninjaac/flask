from flask import Flask,render_template,request
import os
from convert_color_gray_image import Convert_image
app=Flask(__name__)

upload_folder=os.path.join('static','upload')
app.config['upload_folder']=upload_folder

@app.route('/')
def upload_image_html():
    back_image = os.path.join(app.config['upload_folder'], 'monkey_nija_3.png')
    return render_template('convert_page.html',back=back_image)

@app.route('/chance_image',methods=['GET','POST'])
def upload():
    file=request.files['file']
    name=request.files['file'].filename

    if name !='':
        image_folder = os.path.join('static', 'images')
        app.config['upload_folder'] = image_folder
        back_image = os.path.join(app.config['upload_folder'], 'monkey_nija_3.png')
        image_path = os.path.join(app.config['upload_folder'], name)
        file.save(image_path)
        image=Convert_image.color_gray(image_path,name)

        return render_template('convert_page.html',upload_image_src=image_path,image_src=image,back=back_image)

