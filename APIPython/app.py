import pytesseract
import cv2
import tempfile
import os

from flask import Flask, request, send_file, make_response
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
    texto = BuscarTextoImagem(pathtemp)

    nome_arquivo = Criatxt(texto, img.filename)

    caminho_arquivo = os.path.join(app.root_path, nome_arquivo)

    resposta = make_response(send_file(caminho_arquivo, as_attachment=True))
    resposta.headers['Content-Disposition'] = 'attachment; filename=' + nome_arquivo
    return resposta

def BuscarTextoImagem(img):
    path = r"Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path
    texto = pytesseract.image_to_string(img, lang="por")
    print(texto)
    return texto

def CaminhoTemporario(img):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(img.read())
        return temp_file.name

def Criatxt(texto, nome_arquivo):
    nome_arquivo += ".txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    return nome_arquivo

def DeletarArquivo(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print(f"Arquivo '{caminho_arquivo}' deletado com sucesso.")
    else:
        print(f"O arquivo '{caminho_arquivo}' não existe.")

if __name__ == '__main__':
    app.run()