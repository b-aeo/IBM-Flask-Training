'''This server uses data within a flask application instance using dummy data from mockaroo in dictionary format'''

from flask import Flask, make_response, jsonify, request
app = Flask(__name__)


## Data for use in flask app
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

## Defining route for get data method
@app.route("/data")
def get_data():
    '''Method returns number of key value pairs in the data variable with error handling logic'''
    ## Setting up error handling with try, except
    try:
        ## Checks if the data variable contains data
        if data and len(data) > 0:
            ## Returns the number of dictionaries in the data variable
            return {"message": f"Data of length {len(data)} found"}
        else:
            ## If the data variable contains no data returns the below message with unexpected server error status
            return {"message": "Data is empty"}, 500
    except NameError:
        ## Uses the NameError standard error in the event that the variable data contains no value or has no yet been defined when executing
        return {"message": "Data not found"}, 404


@app.route("/name_search")
def name_name():
    ## Creating the query variable to store the query parameter
    query = request.args.get("q")
    ## This is to check if there is data inside the query parameter
    if not query:
    ## Returns error message if query parameter is empty
        return jsonify(message = "Invalid input parameter"), 422

    else:
    ## Defining empty dictionary
        info = {}
    ## Iterates through all dictionaries in data list
        for i in data:
    ## Checks if the dictionary value queried is in the dictionaries
            if query in i.values():
    ## Appends the dictionary to info if the value queried is found
                info.update(i)
    ## Returns the appended dictionary
                return info
    ## The for loop terminates the function in the event that the query is found
    ## in the data placing the return for the 404 person not found error triggers
    ## it in the event that the query is not found in the data        
        return jsonify(message = "Person not found"), 404
    






