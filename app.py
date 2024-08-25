from flask import Flask, request, jsonify
import string

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        # Extract data from the request
        data = request.json
        full_name = data.get('full_name')
        dob = data.get('dob')  # Expected format: 'ddmmyyyy'
        college_email = data.get('college_email')
        college_roll_number = data.get('college_roll_number')
        input_string = data.get('input_string', '')

        # Validate input
        if not full_name or not dob or not college_email or not college_roll_number:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        # Construct user_id in the format full_name_ddmmyyyy
        user_id = f"{full_name.replace(' ', '_').lower()}_{dob}"

        # Create arrays for numbers and alphabets
        numbers = [char for char in input_string if char.isdigit()]
        alphabets = [char for char in input_string if char.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets, default='') if lowercase_alphabets else None

        # Construct the response
        response = {
            "is_success": True,
            "user_id": user_id,
            "college_email": college_email,
            "college_roll_number": college_roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase": highest_lowercase
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    try:
        # Return a simple operation code
        return jsonify({"operation_code": 1}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
