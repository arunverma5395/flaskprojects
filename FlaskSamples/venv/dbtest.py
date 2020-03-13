from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
import yaml

db = yaml.load(open('db.yaml'))

app = Flask(__name__)

mysql.init_app(app)
Bootstrap(app)

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        n = request.form['name']
        p = request.form['pwd']
        return "Name=" + n + "password=" + p
    # cur = mysql.connection.cursor()
    # result_cnt = cur.execute('select name from tblUser')
    # if result_cnt > 0:
    #     users = cur.fetchall()
    #     print(users[0])
    return render_template('index.html')
    # try:
    #     cur = mysql.connection.cursor()
    #     cur.execute("insert into tblUser values (5,'AVerma')")
    #     mysql.connection.commit()
    # except Exception as e:
    #     try:
    #         print(e.args[0])
    #         print(e.args[1])
    #         return None
    #     except IndexError:
    #         print("MySQL Error: %s" % str(e))
    #         return None
    # except TypeError as e:
    #     print(e)
    #     return None
    # except ValueError as e:
    #     print(e)
    #     return None
    # finally:
    #     cur.close()
    #     mysql.connection.close()

    # result_cnt = cur.execute('select * from tblUser')
    # if result_cnt > 0:
    #     users = cur.fetchall()


# return redirect(url_for('about'))
# cursor = mysql.get_db().cursor()


@app.route('/about')
def about():
    fruits = ['Apple', 'Mango', 'Orange']
    return render_template('about.html', fruits=fruits)


@app.route('/css')
def Css():
    # return 'hello world'
    # cursor = mysql.get_db().cursor()
    return render_template('Css.html')


if __name__ == "__main__":
    app.run(debug=True)
