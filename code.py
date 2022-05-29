import qrcode
from PIL import Image

x = "https://youtu.be/NCzgzO1y7yQ"  # the url video
print("The QRcode is saved!: ", x)


def generate_qr(data, img_name="qrCode.png"):
    img = qrcode.make(data)
    img.save(img_name)
    return img


generate_qr(x)
