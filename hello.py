from flask import Flask

# main variable to use.
app = Flask(__name__)

# start creating end-points.

@app.route("/", methods=['GET'])
def hello():
    return "Hello there.!!"

@app.route("/ping", methods=['GET'])
def anything():
    return {"message" : "why are you pinging me?"}


@app.route("/ping", methods=['POST'])
def post():
    pass