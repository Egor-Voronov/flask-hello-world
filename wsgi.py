from flask import Flask

app = Flask(__name__)


@app.route('/<string:exp>')
def calc(exp):
    a = exp[1]

    x, y = int(exp[0]), int(exp[2])

    if a == ':':
        return f'{x / y}'

    elif exp[1] == '*' and not (exp[2] == '*'):
        return f'{x * y}'

    elif a == '+':
        return f'{x + y}'

    elif a == '-':
        return f'{x - y}'

    elif exp[1] == '*' and exp[2] == '*':
        return f'{x ** y}'


if __name__ == '__main__':
    app.run()
