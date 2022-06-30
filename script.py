from turtle import fillcolor
import qrcode
features=qrcode.QRCode(version=1,box_size=40,border=3)
features.add_data('durgansh.xyz')
features.make(fit=True)
generate_image=features.make_image(fill_color="purple",back_color="white")
generate_image.save("image1.png")