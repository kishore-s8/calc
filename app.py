from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return {'result': a + b}
    except:
        return {'error': 'Invalid input'}, 400

@app.route('/')
def health():
    return 'Calculator API is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, need to modify to helloworld differnet fonts code
