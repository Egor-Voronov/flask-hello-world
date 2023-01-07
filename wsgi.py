from flask import Flask, render_template

app = Flask(__name__)

from flask import render_template


@app.route('/<float:a>/')
def index(a):
    return render_template('index.html',
                           r=a,
                           pi=3.14)

if __name__ == '__main__':
    app.run(debug=True)
