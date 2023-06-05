from flask import Flask, session, jsonify, request
from api_handler import get_joke
import random
import string


app = Flask(__name__)


@app.route("/hello")
@app.route("/hello/")
def hello():
    myid = [i for i in string.ascii_letters+string.digits]
    random.shuffle(myid)
    response = {"id": "".join(myid[:5]),
                "value": "Hello, world!"}
    return jsonify(response)


@app.route("/health/readiness")
@app.route("/health/liveness")
def healt():
    response = {"status": "UP"}
    return jsonify(response)


@app.route("/joke")
def joke():
    joke = get_joke()
    response = {"id": "", "joke": ""}
    if joke:
        response["id"] = joke["id"]
        response["joke"] = joke["value"]
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=8091, host='0.0.0.0')