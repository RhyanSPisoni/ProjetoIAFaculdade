import pytesseract
import cv2

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ""

@app.route('/imagem')
def listar_usuarios():
    return

def BuscarTextoImagem():
    imagem = cv2.imread("email.JPG")
    caminho = r"Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = caminho
    texto = pytesseract.image_to_string(imagem, lang="por")
    print(texto)
    return texto

if __name__ == '__main__':
    app.run()