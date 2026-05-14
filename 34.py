import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data("https://github.com/ssandeepsingapur-netizen")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("blue_qr.png")
