from flask.views import MethodView
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL, MySQLdb
from config import KEY_TOKEN_AUTH
import datetime
import time
import bcrypt
import jwt
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'matriculate'

mysql = MySQL(app)

productos = [{"id": 1, "url": "https://www.casdquindio.edu.co/img/slider/foto1.jpg",
                 "nombre": "CASD", "primaria": "jornada unica", "secundaria": "jornada unica","media": "jornada unica"},
        
            ]


class datosUserControllers(MethodView):
    """
        datos
    """

    def get(self):
        return jsonify({"data": productos}), 200



class registroacudeinteUserControllers(MethodView):
    """
        Registro
    """
    def post(self):
        # simulacion de espera en el back con 1.5 segundos
        time.sleep(1)
        content = request.get_json()
        nombres = content.get("nombres")
        apellidos = content.get("apellidos")
        identificacion= content.get("identificacion")
        telefono = content.get("telefono")
        email = content.get("email")
        password = content.get("password")
        direccion= content.get("direccion")
        profesion = content.get("profesion")
        parentesco= content.get("parentesco")
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
        # comandos sql para agregar infomacion a la tabla users
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO acudiente (nombres, apellidos,identificacion, telefono, email, password, direccion, profesion, paretesco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (nombres,apellidos,identificacion,telefono,email,direccion,profesion,parentesco, hash_password))
        mysql.connection.commit()
        cur.close()
        return jsonify({"registro ok": True, "nombres": nombres,"apellidos": apellidos,"direccion":direccion,"parentesco":parentesco, "email": email}), 200
       


class LoginUserControllers(MethodView):
    """
        Login 
    """
    def post(self):
        # simulacion de espera en el back con 1.5 segundos
        user = ""
        time.sleep(1)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")

        # creamos comandos sql para verificar que la informacion que ingresamos sea correcta
        cur = mysql.connection.cursor()
        cur.execute("SELECT nombres, apellidos,identificacion, telefono, email, password, direccion, profesion, paretesco FROM users WHERE email=%s", ([email]))
        user = cur.fetchall()
        user = user[0]
        correo = user[3]
        clave = user[4]
        usuario = {}
        usuario[correo] = {"contraseña":clave} 
        cur.close() 
        # creamos diversos caminos que el sofware puede coger 
        if usuario.get(correo):

            passwordUser = usuario[correo]["contraseña"]

            if bcrypt.checkpw(bytes(str(password), encoding= 'utf-8'), passwordUser.encode('utf-8')):
                
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15), 'correo': correo}, KEY_TOKEN_AUTH , algorithm='HS256')

                return jsonify({"auth": True, "nombre": user[0], "ultinombre": user[1], "celular": user[2], "email": user[3], "token": encoded_jwt}), 200  

            else:  
            
                return jsonify({"auth": False,}), 403

        else:  
            
            return jsonify({"auth": False,}), 401


class datosinstitucionUserControllers(MethodView):
    """
        datos
    """

    def get(self):

        dato=""
        cur = mysql.connection.cursor()
        cur.execute("select nombre,  informacion from institucion where id_institucion = %s")
        dato = cur.fetchall()
        dato = dato[0]
        print ("DATOS DE MYSQL", dato) 

        return jsonify({"data": dato}), 200
