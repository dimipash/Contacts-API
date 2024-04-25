from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_route():
    print('I have received a re quest on the /hello endpoint!')
    return '<h1>Hello from the server!</h1>'

app.run(debug=True)