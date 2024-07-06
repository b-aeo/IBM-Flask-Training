from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

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

@app.get("/count")
def count():
    try:
        counter = 0
        for i in data:
            counter += 1
        return jsonify(message = f"Data count is: {counter}")
        
    except NameError:
        return jsonify( message = "Data not defined" ), 500

## <> within the app decorator creates a dynamic URL, creating a variable which can be
## used in the function this variable is defined as type uuid and called uuid
@app.get("/person/<uuid:uuid>")
def find_by_uuid(uuid):
    ## Defining empty dictionary
    
    info = {}
    ## Iterates through all dictionaries in data list
    for i in data:
    ## Checks if the dictionary value queried is in the dictionaries
        if str(uuid) in i.values():
    ## Appends the dictionary to info if the value queried is found
            info.update(i)
    ## Returns the appended dictionary
            return info
    ## The for loop terminates the function in the event that the query is found
    ## in the data placing the return for the 404 person not found error triggers
    ## it in the event that the query is not found in the data        
    return jsonify(message = "ID not found"), 404
    
## The app delete decorator is for a delete request, it uses the uuid type and variable
## for dynamic routing    
@app.delete("/person/<uuid:uuid>")
def delete_by_uuid(uuid):
    ## To index the list later a count variable is created
    count = 0
    for i in data:
        if str(uuid) in i.values():
            ## Deleting the relevant dictionary when queried ID is found
            del data[count]
            return jsonify(message = str(uuid))
        ## Incrementing the counter if the ID is not found for indexing if it is found
        ## further along the list
        count += 1
    return jsonify(message = "Person not found"), 404

@app.route("/person", methods = ["POST"])
def add_by_uuid():
    ## Using the get_json method to parse the json query
    new_person = request.get_json()

    for i in data:
    ## Check if id has been included in the request
        if "id" in new_person:
    ## Check if the id in the post request is already in the data list
            if new_person[id] == i["id"]:
                return jsonify(message = "Person already stored in data"), 404
        else:
    ## If id is not in the request return message
            return jsonify(message = "Invalid input parameter"), 400    
    ## Append the post request into the list
    data.append(new_person)
    new_person_id = new_person["id"]
    return jsonify(message = f"Person added with id: {new_person_id}")

## Creating a custome error handler to overide default html error response for 404 errors
@app.errorhandler(404)
## The function takes in the error
def handle_404(error):
## Desired error response
    return jsonify(message = "Resource not found"), 404

    

