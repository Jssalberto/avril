from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/index/', methods=["GET"])
def index():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)