from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    request_data = request.get_json()
    data = request_data.get('data', [])

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase_alphabet = sorted(
        [char for char in alphabets if char.islower()],
        key=lambda x: x[-1]
    )[-1:] if alphabets else []

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
