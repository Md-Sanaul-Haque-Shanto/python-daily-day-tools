import qrcode
from PIL import Image

logo = Image.open('icon.jpg')
basewidth = 75
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth,hsize), Image.ANTIALIAS)
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data('yourdomain')
qr_big.make()
img_qr_big = qr_big.make_image(fill_color='#0b4e39',black_color="white").convert('RGB')
pos = ((img_qr_big.size[0]-logo.size[0])//2, (img_qr_big.size[1]-logo.size[1])//2)
img_qr_big.paste(logo, pos)
img_qr_big.save('branded_qr.jpg')