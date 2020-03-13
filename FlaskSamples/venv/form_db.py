from flask import Flask, request, jsonify, render_template, url_for, redirect, Response, Request, flash
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
import yaml

db = yaml.load(open('db.yaml'))
app = Flask(__name__)
Bootstrap(app)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = db['mysql_secretkey']
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def getdata():
    try:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['name']
            cur = mysql.connection.cursor()
            cur.execute("insert into tblUser (id,name) values (%s, %s)", (id, name))
            mysql.connection.commit()
            flash("User added successfully !!", 'success')
    except:
        flash("failed to insert data", 'danger')

    return render_template('index.html')


@app.route('/employees')
def getemployees():
    try:
        cur = mysql.connection.cursor()
        r = cur.execute("select * from tblUser")
        if r > 0:
            employees = cur.fetchall()
            return render_template('users.html', employees=employees, count=r)
        else:
            return render_template('users.html', count=0)
    except:
        print('some error')
        # except mysql.connector.Error as e:
        # print("Error code:", e.errno)  # error number
        # print("SQLSTATE:", e.sqlstate)  # SQLSTATE
        # print("Error:", e)  # SQLSTATE
        # s = str(e)
        # print("Error:", s)  # # errno, sqlstate, msg value


if __name__ == "__main__":
    app.run(debug=True, port=8500)
