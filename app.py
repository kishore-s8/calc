from flask import Flask, request, jsonify

app = Flask(__name__)

def get_numbers():
    try:
        a = float(request.args.get('a', None))
        b = float(request.args.get('b', None))
        if a is None or b is None:
            raise ValueError("Missing parameter")
        return a, b
    except (TypeError, ValueError):
        return None, None

@app.route('/add')
def add():
    a, b = get_numbers()
    if a is None or b is None:
        return jsonify({'error': 'Invalid or missing parameters a and b'}), 400
    return jsonify({'result': a + b})

@app.route('/subtract')
def subtract():
    a, b = get_numbers()
    if a is None or b is None:
        return jsonify({'error': 'Invalid or missing parameters a and b'}), 400
    return jsonify({'result': a - b})

@app.route('/multiply')
def multiply():
    a, b = get_numbers()
    if a is None or b is None:
        return jsonify({'error': 'Invalid or missing parameters a and b'}), 400
    return jsonify({'result': a * b})

@app.route('/divide')
def divide():
    a, b = get_numbers()
    if a is None or b is None:
        return jsonify({'error': 'Invalid or missing parameters a and b'}), 400
    if b == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    return jsonify({'result': a / b})

@app.route('/')
def health():
    return 'Calculator API is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
