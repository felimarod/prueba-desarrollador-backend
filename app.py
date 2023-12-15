from services.tutorial_controlador import obtener_tutoriales, obtener_tutorial_por_id, agregar_tutorial, actualizar_tutorial, eliminar_tutorial_por_id
from services.detalle_controlador import agregar_detalle, eliminar_detalle_por_id, actualizar_detalle, obtener_detalle_por_id
from flask import Flask, jsonify, request
from services.db import crear_tablas


app = Flask(__name__)


@app.route('/api/tutorial', methods=["GET"])
def get_tutoriales():
    result = obtener_tutoriales()
    return jsonify(result)


@app.route('/api/tutorial/<id>', methods=["GET"])
def get_tutorial(id):
    result = obtener_tutorial_por_id(id)
    return jsonify(result)


@app.route('/api/tutorial', methods=["POST"])
def insertar_tutorial():
    data = request.get_json()
    tema = data["tema"]
    descripcion = data["descripcion"]
    titulo = data["titulo"]
    visible = data["visible"]
    id_detalle = agregar_detalle(data["nombre_autor"])
    result = agregar_tutorial(tema, descripcion, titulo, visible, id_detalle)
    return jsonify(result)


@app.route('/api/tutorial', methods=["PUT"])
def modificar_tutorial():
    data = request.get_json()
    id = data["id"]
    tema = data["tema"]
    descripcion = data["descripcion"]
    titulo = data["titulo"]
    visible = data["visible"]
    nombre_autor = data["nombre_autor"]

    # Necesario para poder modificar el autor del tutorial
    tutorial = obtener_tutorial_por_id(id)
    id_detalle = tutorial[5]
    actualizar_detalle(id_detalle, nombre_autor)

    result = actualizar_tutorial(
        id, tema, descripcion, titulo, visible, id_detalle)
    return jsonify(result)


@app.route('/api/tutorial/<id>', methods=["DELETE"])
def eliminar_tutorial(id):
    tutorial = obtener_tutorial_por_id(id)
    eliminar_detalle_por_id(tutorial[5])
    result = eliminar_tutorial_por_id(id)
    return jsonify(result)


@app.route('/api/detalle/<id>', methods=["GET"])
def get_detalle(id):
    detalle = obtener_detalle_por_id(id)
    return jsonify(detalle)


@app.after_request
def after_request(response):
    # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    crear_tablas()
    app.run(host='0.0.0.0', port=8000, debug=True)
