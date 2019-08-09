from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/hello/<name>')
def index(name):
    return "Hello " + name


@app.route('/profile')
def profile():
    myName = request.args.get('name')
    return render_template('introduction.html',
                           myNameInHtml = myName)



if __name__ == '__main__':
    app.run()