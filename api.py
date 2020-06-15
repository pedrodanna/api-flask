from flask import Flask, render_template, request, jsonify

#Referencing this file
app = Flask(__name__)

#App home index
@app.route('/', methods=['GET'])
#Index page fucntion
def index():
    return render_template('index.html')

#Executing the app
if __name__ == "__main__":
    #Running the app
    app.run(debug=True)