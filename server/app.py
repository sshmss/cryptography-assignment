import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from itertools import permutations
from pathlib import Path
import time
from ntpath import join
import string
import random


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_url_path="/app", static_folder="app")
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/task1', methods=['POST'])
def task_one():
    data = request.get_json()
    card_no = data['card_no']
    if len(card_no) != 16 or not card_no.isdigit():
        return jsonify({'data': 'Invalid characters or length does not match 16'}), 400
    return jsonify({'data': "Card number is valid"})


@app.route('/task4', methods=['POST'])
def task_four():
    start = time.time()
    data = request.get_json()
    possible_inputs = data['possible_inputs']
    input_hash = data['hash']
    perms = []
    if not Path(f'rainbow_table_{possible_inputs}.txt').is_file():
        for i in range(1, len(possible_inputs)+1):
            perms += [''.join(p) for p in permutations(possible_inputs, i)]
        with open(f'rainbow_table_{possible_inputs}.txt', 'w') as file:
            for p in perms:
                file.writelines(f'{p},{hasher(p, possible_inputs)}\n')
    with open(f'rainbow_table_{possible_inputs}.txt', 'r') as file:
        for line in file:
            pair = line.strip().split(',')
            password = pair[0]
            hash = pair[1]
            if input_hash == hash:
                return jsonify({'data': f'{input_hash} cracked in {round(time.time() - start, 2)}s. The password is {password}'})
    return jsonify({'data': "Hash not in rainbow table."})


def hasher(perm, possible_inputs):
    hashed = perm[-1] * 2
    hashed += perm
    hashed = hashed[::-1]
    if len(hashed) > len(possible_inputs):
        hashed = hashed[: len(possible_inputs)]
    while True:
        if len(hashed) < len(possible_inputs):
            hashed += possible_inputs[-len(hashed)]
        else:
            break
    return hashed


@app.route('/task3', methods=['POST'])
def task_three():
    start = time.time()
    data = request.get_json()
    password = data['password']

    alphanum = string.ascii_lowercase + string.digits
    alphanum_list = list(alphanum)

    result_password = ""
    iteration = 0
    while(result_password != password):
        result_password = random.choices(alphanum_list, k=len(password))
        iteration = iteration + 1

        if(result_password == list(password)):
            final_password = ''.join(result_password)
            return jsonify({'data': f'Result password is {final_password}. Brute forced in {round(time.time() - start, 2)}s after {iteration} attempts.'})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run()
