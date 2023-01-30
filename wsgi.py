from flask import Flask, request, jsonify

import datetime

app = Flask(__name__)

@app.route("/api/", methods=["GET"])
def render_send():
    request_args = request.args or None
    period = []

    for key, value in request_args.items():
        period.append(value)

    start = period[0].split('-')
    end = period[1].split('-')

    start = datetime.date(int(start[0]), int(start[1]), int(start[2]))
    end = datetime.date(int(end[0]), int(end[1]), int(end[2]))

    arr = [datetime.date(2017, 10, 3), datetime.date(2021, 10, 3), datetime.date(2027, 10, 3)]

    res = []

    for e in arr:
        if start <= e <= end:
            res.append(e)

    print(end)
    return res


if __name__ == '__main__':
    app.run(debug=True)
