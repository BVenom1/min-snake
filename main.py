import qrcode
import base64
import sys

v = 40

with open('index.html', 'r') as file:
    b64 = base64.b64encode(file.read().encode())
    b64_str = f'{b64}'.split("'")[1]
    print(sys.getsizeof(b64_str))
    qr = qrcode.QRCode(version=v, box_size=5, border=10, error_correction=qrcode.ERROR_CORRECT_L)
    qr.add_data(f'data:text/html;base64,{b64_str}')
    qr.make(fit=True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save(f'min-sanke-{v}.png')