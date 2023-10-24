from services.tutorial_controlador import obtener_tutoriales
from flask import Flask,jsonify,request
from services.db import crear_tablas


app = Flask(__name__)

@app.route('/tutoriales', methods=["GET"])
def get_tutoriales():
    tutoriales = obtener_tutoriales()
    return jsonify(tutoriales)


if __name__ == "__main__":
    crear_tablas()
    app.run(debug=True)