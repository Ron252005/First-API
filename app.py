from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

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
    marks_list = []
    
    # Create a dictionary for quick lookup
    student_dict = {student['name']: student['marks'] for student in student_data}
    
    # Maintain the order of names as in the request
    for name in names:
        if name in student_dict:
            marks_list.append(student_dict[name])
        else:
            marks_list.append(None)  # or you could use a sentinel value like -1
    
    result["marks"] = marks_list
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
