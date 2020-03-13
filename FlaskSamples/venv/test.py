from flask import Flask, jsonify, request

app = Flask(__name__)

a = [1, 2, 4]


@app.route('/')
def hello_world():
    return "wor"


@app.route('/add', methods=["POST"])
def add():
    dict = request.get_json()
    x = dict["x"]
    y = dict["y"]
    z = x + y
    retjson = {
        "sum": z
    }
    return jsonify(retjson), 404


@app.route('/arun')
def hello_arun():
    cnt = 100
    retvar = {
        "name": "arun V",
        "addresses": [
            {
                "City": "Hisar",
                "floor_people_count": [
                    {
                        "floor#": cnt,
                        "people_count": 3
                    },
                    {
                        "floor#": 2,
                        "people_count": 4
                    }
                ]
            },
            {
                "City": "Ghaziabad",
                "floor_people_count": [
                    {
                        "floor#": 2,
                        "people_count": 3
                    },
                    {
                        "floor#": 3,
                        "people_count": 0
                    }
                ]
            }
        ]

    }
    return jsonify(retvar)


if __name__ == "__main__":
    app.run(debug=True)
