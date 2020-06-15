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

#Executing the app
if __name__ == "__main__":
    #Running the app
    app.run(debug=True)