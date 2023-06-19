import pytesseract
import cv2

imagem = cv2.imread("email.JPG")

caminho = r"Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = caminho
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)