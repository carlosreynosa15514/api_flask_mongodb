from flask import Flask
from flask_mongo import PyMongo
# Se inicializa la app
app = Flask(__name__)

# Cadena de conexion
app.config['MONGO_URI']='mongodb://localhost:27017/pythonmongodb'
mongo = PyMongo(app) 


# Se crea el servidor app
if __name__ == "__main__":
    app.run(debug=True) # Para que se actualice la app sin reiniciar servidor
    