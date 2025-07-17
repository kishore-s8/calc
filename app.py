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
def hello():
    # Return Hello World in multiple font styles using HTML
    return '''
    <html>
        <head><title>Hello</title></head>
        <body>
            <h1 style="font-family: Arial;">Hello, World! (Arial)</h1>
            <h1 style="font-family: Courier New;">Hello, World! (Courier New)</h1>
            <h1 style="font-family: Georgia;">Hello, World! (Georgia)</h1>
            <h1 style="font-family: Times New Roman;">Hello, World! (Times New Roman)</h1>
            <h1 style="font-family: Verdana;">Hello, World! (Verdana)</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
