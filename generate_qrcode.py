import pyqrcode
import png

from pyqrcode import QRCode

QR_string = input("Enter URL: ")
url = pyqrcode.create(QR_string)
url.png(r"qrcode.png", scale = 8)