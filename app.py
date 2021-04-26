from flask import Flask, request, jsonify
from flask_mysqldb import MySQL, MySQLdb
from routes import *
from flask_cors import CORS

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'matriculate'

mysql = MySQL(app)

CORS(app, resources={r"/*": {"origins": "*"}})


app.add_url_rule(user["datos_user"], view_func=user["datos_user_controllers"])
app.add_url_rule(user["registroacudiente_user"], view_func=user["registroacudiente_user_controllers"])
app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
#app.add_url_rule(user["anuncio_user"], view_func=user["anuncio_user_controllers"])
app.add_url_rule(user["datosinstitucion_user"], view_func=user["datoinstitucion_user_controllers"])