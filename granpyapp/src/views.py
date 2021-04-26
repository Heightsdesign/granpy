from flask import Flask, render_template, request, jsonify, make_response
import json
from compiler import Compiler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/question/", methods=["POST"])    
def ask_question():
    
    req = request.get_json()

    data = Compiler(req).compile()

    print(data['lat'])

    res = make_response(jsonify({"message": "JSON received"}), 200)

    return res


if __name__ == "__main__":
    app.run(debug=True)