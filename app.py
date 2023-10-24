from services.tutorial_controlador import obtener_tutoriales, obtener_tutorial_por_id, agregar_tutorial, actualizar_tutorial, eliminar_tutorial_por_id
from services.detalle_controlador import agregar_detalle, eliminar_detalle_por_id, actualizar_detalle
from flask import Flask, jsonify, request
from services.db import crear_tablas


app = Flask(__name__)


@app.route('/api/tutorial', methods=["GET"])
def get_tutoriales():
    tutoriales = obtener_tutoriales()
    return jsonify(tutoriales)


@app.route('/api/tutorial/<id>', methods=["GET"])
def get_tutorial(id):
    tutorial = obtener_tutorial_por_id(id)
    return jsonify(tutorial)


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
    id_detalle = tutorial["id_detalle"]
    actualizar_detalle(id_detalle, nombre_autor)

    result = actualizar_tutorial(
        id, tema, descripcion, titulo, visible, id_detalle)
    return jsonify(result)


@app.route('/api/tutorial/<id>', methods=["DELETE"])
def eliminar_tutorial(id):
    tutorial = obtener_tutorial_por_id(id)
    eliminar_detalle_por_id(tutorial["id_detalle"])
    eliminar_tutorial_por_id(id)
    return jsonify(tutorial)


if __name__ == "__main__":
    crear_tablas()
    app.run(debug=True)
