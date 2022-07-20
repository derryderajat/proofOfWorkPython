import pyperclip as pyp
import json
from datetime import datetime
from hashlib import sha256
import os
import uuid
from flask import Flask, request, jsonify
import splitName
import base64
from aes import AESCipher
UPLOAD_FOLDER = "./upload"
FILES_FOLDER = "./files"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["FILES_FOLDER"] = FILES_FOLDER
data = {}


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file1" not in request.files:
            return "there is no file1 in form!"
        file1 = request.files["file1"]
        file_type = file1.content_type
        new_name = splitName.splitType(file_type)
        data["data"] = {}
        data["data"]['fileName'] = file1.filename.split('.')[0]
        file1.filename = new_name
        path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
        
        file1.save(path)
        print(path)
        with open(path, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
        key = "000"
        data["data"]['key'] = key
        aes = AESCipher(key)
        encrypt_img = aes.encrypt(str(b64_string))
        decrypt = aes.decrypt(encrypt_img)
        print("Decripted")
        data["data"]["img"] = str(decrypt)
        data["timestamp"] = datetime.utcnow().isoformat()
        data["prev_hash"] = None
        id_ = str(uuid.uuid4())
        id_ = id_.split("-")
        id_ = "".join(id_)
        data["data"]["id"] = id_ 
        data["nonce"] = str(uuid.uuid4())
        data["data"]["hash"] = sha256(json.dumps(data).encode()).hexdigest()
        json_path = os.path.join(app.config["FILES_FOLDER"], "data.json")
        with open(json_path, "w") as outfile:
            json.dump(data, outfile)
        return data
    return """
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    """

@app.route("/getImage", methods=[   "GET", "POST"])
def getImage():
    with open("./files/data.json") as fp:
        dictObj = json.load(fp)
    data = json.dumps(dictObj, indent = 4) 
    print(type(data))
    
    return jsonify(data)


if __name__ == "__main__":
    app.run()