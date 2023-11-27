from flask import Flask, jsonify
from models.usuarios import Usuarios

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/users', methods=['GET'])
def get_users():
    users = Usuarios.get_users()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
