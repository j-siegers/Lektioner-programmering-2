from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'


@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'Johan Siegers',
        'email': 'j-siegers@outlook.com'
    }

    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200


@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201
