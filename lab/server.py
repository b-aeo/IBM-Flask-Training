
##import the flask library with flask and jsonify modules
from flask import Flask, jsonify
## Creating an application instance using the flask funciton and __name__ variable
## This stores the instance in the app variable
app = Flask(__name__)
##Defining the route path for the function index
@app.route("/")
def index():
    return "hello world"
##Defining the route path for the function no_content
@app.route("/no_content")
def no_content():
##Using the jsonify function to return a message in json
    return jsonify( message = "No content found"), 204

