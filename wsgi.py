from flask import Flask, request, jsonify

import datetime

app = Flask(__name__)

metrika = dict[
    {
        'phone': '123',
        'utm_campaign': '1'
    },
    {
        'phone': '1234',
        'utm_campaign': '2'
    },
    {
        'phone': '12345',
        'utm_campaign': '3'
    },
]

@app.route("/api/", methods=["GET"])
def render_send():
    next_parameter = request.args or None
    print(next_parameter)
    print(datetime.date.today())

    json_string = ("""
    [
        {
            "phone": "123",
            "utm": "1"
        },
         {
            "phone": "1234",
            "utm": "2"
        },
         {
            "phone": "12345",
            "utm": "3"
        }
    ]
    """)

    return jsonify([{'phone': item.phone, 'test': datetime.date.today(), 'utm_campaign': item.utm} for
                    item in json_string])


if __name__ == '__main__':
    app.run(debug=True)
