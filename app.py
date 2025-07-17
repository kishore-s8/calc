
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify(result=a + b)
    except ValueError:
        return jsonify(error='Invalid input. Please provide numbers.'), 400

@app.route('/')
def health():
    return 'Calculator API is running!'

# if __name__ == '__main__':
#    # app.run(host='0.0.0.0', port=9090)
# app.run(host='0.0.0.0', port=9090)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)


