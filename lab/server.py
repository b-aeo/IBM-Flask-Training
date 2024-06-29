'''This server project is to experiment with creating a range of flask application instances and assigning HTTP codes'''

## Import the flask library with flask and jsonify modules
from flask import Flask, jsonify, make_response
## Creating an application instance using the flask funciton and __name__ variable
## This stores the instance in the app variable
app = Flask(__name__)
## Defining the route path for the method index
@app.route("/")
def index():
    return "hello world"
## Defining the route path for the method no_content
@app.route("/no_content")
def no_content():
## Using the jsonify function to return a message in json
## ", 204" at the end of the line assigns error code 204 to the output
    return jsonify( message = "No content found"), 204

## Defining route for method explicit
@app.route("/exp")
def index_explicit():
    ## Using jsonify and make_response methods to return a json message and specify status code
    ## The response is stored in the res variable
    res = make_response(jsonify(message = " Testing if this json code works"))
    ## Assigning the status code 200 to the response
    res.status_code = 200
    return res

