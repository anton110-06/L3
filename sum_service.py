from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def calculate_sum():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        return f"Result: {result}!", 200
    except (TypeError, ValueError):
        return "Invalid parameters. Please provide numbers for 'a' and 'b'.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
