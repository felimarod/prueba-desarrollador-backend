from services.tutorial_controlador import obtener_tutoriales, obtener_tutorial_por_id, agregar_tutorial, actualizar_tutorial, eliminar_tutorial_por_id
from services.detalle_controlador import agregar_detalle
from flask import Flask, jsonify, request
from services.db import crear_tablas


app = Flask(__name__)


@app.route('/tutoriales', methods=["GET"])
def get_tutoriales():
    tutoriales = obtener_tutoriales()
    return jsonify(tutoriales)


@app.route('/tutorial', methods=["POST"])
def insertar_tutorial():
    data = request.get_json()
    tema = data["tema"]
    descripcion = data["descripcion"]
    titulo = data["titulo"]
    visible = data["visible"]
    id_detalle = agregar_detalle(data["nombre_autor"])
    result = agregar_tutorial(tema, descripcion, titulo, visible, id_detalle)
    return jsonify(result)

@app.route('/tutorial', methods=["PUT"])
def modificar_tutorial():
    data = request.get_json()
    id = data["id"]
    tema = data["tema"]
    descripcion = data["descripcion"]
    titulo = data["titulo"]
    visible = data["visible"]
    id_detalle = data["id_detalle"]
    result = actualizar_tutorial(id,tema, descripcion, titulo, visible, id_detalle)
    return jsonify(result)

if __name__ == "__main__":
    crear_tablas()
    app.run(debug=True)

