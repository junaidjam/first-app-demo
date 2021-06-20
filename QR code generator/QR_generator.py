import qrcode

data = "you are a good guy"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(fill_color = 'red', back_color = "black")

img.save("E:/PycharmProjects/6 quick projects/QR code generator/")