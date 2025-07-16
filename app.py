from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World Different Fonts</title>
    <style>
        .font1 { font-family: Arial, sans-serif; }
        .font2 { font-family: 'Courier New', Courier, monospace; }
        .font3 { font-family: 'Times New Roman', Times, serif; }
        .font4 { font-family: 'Comic Sans MS', cursive, sans-serif; }
        .font5 { font-family: Georgia, serif; }
    </style>
</head>
<body>
    <h1 class="font1">Hello World (Arial)</h1>
    <h1 class="font2">Hello World (Courier New)</h1>
    <h1 class="font3">Hello World (Times New Roman)</h1>
    <h1 class="font4">Hello World (Comic Sans MS)</h1>
    <h1 class="font5">Hello World (Georgia)</h1>
</body>
</html>
"""

@app.route('/')
def hello_world():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
