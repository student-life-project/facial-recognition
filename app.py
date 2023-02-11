import json
from flask import Flask, jsonify, request

from src.create_images import create_images
from src.facial_recognition import facial_recognition

app = Flask(__name__)


@app.route('/user-recognition', methods=["POST"])
def user_recognition():
    face_image_base64 = request.json["faceImage"]
    id_card_image_base64 = request.json["idCardImage"]

    create_images(face_image_base64, id_card_image_base64)

    result = facial_recognition(
        "images/face_image.png", "images/id_card_image.png")

    response = {
        "response": json.dumps(bool(result))
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)