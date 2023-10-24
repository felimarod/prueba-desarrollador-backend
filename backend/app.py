from flask import Flask, jsonify, request
from services.db import crear_tablas


app = Flask(__name__)


if __name__ == "__main__":
    crear_tablas()
    app.run(debug=False)
