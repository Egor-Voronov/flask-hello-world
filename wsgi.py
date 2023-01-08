from flask import Flask, render_template, request, abort

app = Flask(__name__)

from flask import render_template


@app.route('/', methods=['get', 'post'])
def index():
    server_message = ''
    client_message = ''

    if request.method == 'POST':
        client_message = request.form.get('message')

    if client_message == 'hi':
        server_message = 'hello'
    elif client_message != '' :
        server_message = 'how are you?'

    return render_template('index.html',
                           message = server_message
                           )

if __name__ == '__main__':
    app.run(debug=True)
