from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Load the data from data.json
with open('data.json', 'r') as file:
    student_data = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    result = {}
    list = []
    for student in student_data:
        if student['name'] in names:
            list.append(student['marks'])
    for name in names:
        if name not in result:
            result[name] = "Not found"
    result["name"] = list
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)