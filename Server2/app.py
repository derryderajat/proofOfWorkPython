from flask import Flask, jsonify
from datetime import datetime
from hashlib import sha256
import requests
import json
import os
import uuid
from aes import AESCipher
app = Flask(__name__)
import pyperclip
from Blockchain import Blockchain as Bc
@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/mining/<num>", methods=['POST'])
# def mining():
#     pass
@app.route('/mining', methods=['GET','POST'])
def allow():
    response_API = requests.get("http://127.0.0.1:5000/getImage").json()
    # print(response_API.keys())
    # response_API
    data = json.loads(response_API)
    aes = AESCipher("000")
    id_ = createId()
    createFolder(id_)
    bc = Bc()
    bc.proof_of_work()
    res = bc.chain[-1]
    
    # block["data"] = {}
    img = data["data"]["img"]
    res['data'] = {}
    res['data']['img'] = img
    res["prev_hash"] = data['data']['hash']
    res["nonce"] = createId()
    res["timestamp"] = datetime.utcnow().isoformat()
    
    print(type(img))
    json_path = os.path.join("./blocks/",id_ )
    json_path = os.path.join(json_path, "1.json")
    with open(json_path, "w") as outfile:
            json.dump(res, outfile)

    pyperclip.copy(img)
    
    print(data['data'].keys())
    
    return "Data mined and image base64 already copied"

def createFolder(idx):
    path = "./blocks/"
    path = os.path.join(path, idx)
    os.mkdir(path)
    
def createJson(idx,data):
    pass    
    
def createId():
    id_ = str(uuid.uuid4())
    id_ = id_.split("-")
    id_ = "".join(id_)
    return str(id_)


def proof_of_work(block):
    while True:
        new_block = block
        if new_block["hash"].startswith("00"):
            break
    return new_block

if __name__ == '__main__':
    app.run(host="localhost", port=8000)