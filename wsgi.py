from flask import Flask, render_template, request, abort

app = Flask(__name__)

from flask import render_template

news = {}

@app.route("/", methods=["POST", "GET"])
def render_send():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        news[title] = content
        return render_template('index.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)
