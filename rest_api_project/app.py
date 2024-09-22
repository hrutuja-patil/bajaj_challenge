from flask import Flask, request, jsonify
import base64
import filetype

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post_request():
    data = request.json.get("data", [])
    file_b64 = request.json.get("file_b64", "")

    # Response template
    response = {
        "is_success": True,
        "user_id": "Hrutuja_01122003",  # Update to your format
        "email": "ph7012@srmist.edu.in",  # Your email
        "roll_number": "RA2111003011898",  # Your roll number
        "numbers": [],
        "alphabets": [],
        "highest_lowercase_alphabet": [],
        "file_valid": False,  # Default to False
        "file_mime_type": "",
        "file_size_kb": "0"
    }

    # Extract numbers and alphabets
    response["numbers"] = [item for item in data if item.isdigit()]
    response["alphabets"] = [item for item in data if item.isalpha()]

    # Find highest lowercase alphabet
    lowercase_alphabets = [item for item in response["alphabets"] if item.islower()]
    if lowercase_alphabets:
        response["highest_lowercase_alphabet"] = [max(lowercase_alphabets)]

    # Handle file validation
    if file_b64:
        try:
            file_data = base64.b64decode(file_b64)
            response["file_size_kb"] = len(file_data) / 1024

            kind = filetype.guess(file_data)
            if kind:
                response["file_valid"] = True
                response["file_mime_type"] = kind.mime
            else:
                response["file_valid"] = False
        except Exception as e:
            response["file_valid"] = False

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get_request():
    return jsonify({
        "operation_code": 1
    })

if __name__ == '__main__':
    app.run(debug=True)

