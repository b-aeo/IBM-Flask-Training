
##import the flask library with flask and jsonify modules
from flask import Flask, jsonify, make_response
## Creating an application instance using the flask funciton and __name__ variable
## This stores the instance in the app variable
app = Flask(__name__)
##Defining the route path for the method index
@app.route("/")
def index():
    return "hello world"
##Defining the route path for the method no_content
@app.route("/no_content")
def no_content():
##Using the jsonify function to return a message in json
## , 204 at the end of the line assigns error code 204 to the output
    return jsonify( message = "No content found"), 204

##defining route for method make_response
@app.route("/exp")
def index_explicit():
    res = make_response(jsonify(message = " Testing if this json code works"))
    res.status_code = 200
    return res

