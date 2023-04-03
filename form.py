from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['formdata']

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    science = request.form.get('science')
    math = request.form.get('math')
    english = request.form.get('english')
    programming = request.form.get('programming')

    # Insert the form data into the MongoDB collection
    collection.insert_one({
        'science': science,
        'math': math,
        'english': english,
        'programming': programming
    })

    return f'Science: {science}, Math: {math}, English: {english}, Programming: {programming}'

if __name__ == '__main__':
    app.run(debug=True)
