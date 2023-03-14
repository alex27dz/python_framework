from flask import Flask, jsonify

app = Flask(__name__)  # creating the flask app

@app.route('/')  # default route
def index():
    return jsonify({'hi': 'alex'})

@app.route('/my-endpoint')
def endpoint():
    return 'hello world'

if __name__ == '__main__':
    app.run()

