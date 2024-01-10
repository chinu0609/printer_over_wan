from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField
from werkzeug.utils import secure_filename
from printer import printer


app = Flask("Ganesha")
app.config["SECRET_KEY"] = "ganu"


class FileForm(FlaskForm):
    file =  FileField(label="your file here")
    
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/upload",methods =["GET","POST"])
def upload():  
    form = FileForm() 
  
    if form.validate_on_submit():

      
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/'+filename)
        printer(filename) 
        return redirect(url_for('upload'))
    return render_template("index.html",form=form)
   
        




if __name__ == "__main__":
    app.run(debug=True,host = "your ip assigned by the router here")
