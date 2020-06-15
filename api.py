from flask import Flask, render_template, request, jsonify

import json

#Importing JSON data from a file
with open('data.json') as json_file:
    data = json.load(json_file)

#Referencing this file
app = Flask(__name__)

#App home index
@app.route('/', methods=['GET'])
#Index page function
def index():
    return render_template('index.html')

#App all API's page
@app.route('/api/all', methods=['GET'])
#All API's page function
def all():
    #Returning data in JSON format
    return jsonify(data)

#App specific definiton page
@app.route('/api/def', methods=['GET'])
#Specific definiton page fucntion
def api_title():
    # If title is provided, assign it to a variable
    if 'title' in request.args:
        title = request.args['title']
    # If no ID is provided, display an error in the browser
    else:
        return "Error: No API found with currency URL"

    #Empty list for future use
    api_list = []

    #Loop through the data and match results that fit the requested ID
    for defs in data:
        if defs['title'] == title:
            print("Foi")
            api_list.append(defs)

    return jsonify(api_list)

#Executing the app
if __name__ == "__main__":
    #Running the app
    app.run(debug=True)