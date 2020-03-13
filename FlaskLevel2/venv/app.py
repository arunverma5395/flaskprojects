from flask import Flask, request, render_template, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml, os
import pandas as pd
from werkzeug.utils import secure_filename

db = yaml.load(open('db.yaml'))
app = Flask(__name__)
Bootstrap(app)

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = db['mysql_secretkey']
app.config['UPLOAD_FOLDER'] = '/home/dkusr/'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        if request.method == 'POST':
            # p1 = request.form['p1']
            # p2 = request.form['p2']
            inputfile = request.files['inputfile']
            orig_name = inputfile.filename
            filename = secure_filename(orig_name)
            fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            inputfile.save(fullpath)
            df = pd.read_csv(fullpath)

            # fstring = inputfile.read()
            # return fstring
            flash('Saved Successfully!!', 'success')
    except:
        flash("failed to save file", 'danger')

    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True, port=8500)
