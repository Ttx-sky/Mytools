from flask import Flask, jsonify, request
from getip import GETIP

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    key = request.args.get('key')
    if key != '123321':
        return jsonify({'status': False, 'data': None})
    ok_ip = GETIP().run()
    return jsonify({'status': True, 'data': {'http': ok_ip}})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8456)
