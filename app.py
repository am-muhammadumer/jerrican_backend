from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded API key
API_KEY = "urem98u5m-jrlekjm09u540-9ojrlkejr0943uior0"

@app.route('/xyz', methods=['GET'])
def get_api_key():
    """
    Endpoint to return the hardcoded API key.
    """
    return jsonify({"api_key": API_KEY})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
