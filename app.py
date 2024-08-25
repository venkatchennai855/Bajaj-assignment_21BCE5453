from flask import Flask, request, jsonify
import string

app = Flask(__name__)

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        data = request.json

        # Extract data from the request
        user_id = data.get('user_id')
        college_email = data.get('college_email')
        college_roll_number = data.get('college_roll_number')
        input_string = data.get('input_string', '')

        # Create arrays for numbers and alphabets
        numbers = [char for char in input_string if char.isdigit()]
        alphabets = [char for char in input_string if char.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets, default='') if lowercase_alphabets else None

        # Construct the response
        response = {
            'status': 'success',
            'user_id': user_id,
            'college_email': college_email,
            'college_roll_number': college_roll_number,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_lowercase': highest_lowercase
        }
        return jsonify(response)

    elif request.method == 'GET':
        # Return a simple operation code
        return jsonify({'operation_code': 200})

if __name__ == '__main__':
    app.run(debug=True)
