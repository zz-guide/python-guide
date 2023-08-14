from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!123'


@app.route('/detail', methods=['GET'])
def detail():  # put application's code here
    return jsonify({"id": 1, "name": "许磊"})  # 返回布尔值


if __name__ == '__main__':
    app.run()
