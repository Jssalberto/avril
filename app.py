from flask import Flask
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from Model.Usuario.Usuario import Usuario
app = Flask(__name__)


@app.route('/index/', methods=["GET"])
def index():
    return render_template('inicio.html')


@app.route('/password/<password>/', methods=["GET"])
def password(password):
    return f'Tu passwor is: {generate_password_hash(password)}'

@app.route('/usuario', methods=["GET"])
def usuario():
    pass
if __name__ == '__main__':
    app.run(debug=True)