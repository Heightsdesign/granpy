from flask import render_template, request, jsonify, make_response
from src.compiler import Compiler
from src import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/question/", methods=["POST"])
def ask_question():

    req = request.get_json()

    data = Compiler(req).compile()

    res = make_response(jsonify(data), 200)

    return res
