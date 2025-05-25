from flask import Flask, request

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def greeting():
    name = request.args.get('name', 'Anonymous')
    return f"Привет, {name}!\n", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
