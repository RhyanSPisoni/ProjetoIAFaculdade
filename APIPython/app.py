import pytesseract
import cv2
import tempfile

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def hello():
    return ""

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'Nenhuma imagem enviada', 400

    img = request.files['image']
    pathtemp = CaminhoTemporario(img)

    return BuscarTextoImagem(pathtemp)

def BuscarTextoImagem(img):
    path = r"Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path
    texto = pytesseract.image_to_string(img, lang="por")
    print(texto)
    return texto

def CaminhoTemporario(img):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(img.read())
        return  temp_file.name

if __name__ == '__main__':
    app.run()