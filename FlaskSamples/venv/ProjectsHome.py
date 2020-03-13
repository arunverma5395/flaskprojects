from flask import Flask, request, jsonify, render_template, url_for, redirect
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
mysql = MySQL(app)
