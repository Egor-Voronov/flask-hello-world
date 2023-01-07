from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<float:num>/')
def index(num):
    return render_template('index.html',
                          number = num * 2,
                          text = f"Ваше число {num}, умноженное на 2:",
                          )


if __name__ == '__main__':
    app.run(debug=True)
