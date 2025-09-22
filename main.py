import base64
import sys

with open('index.html', 'r') as file:
    b64 = base64.b64encode(file.read().encode())
    b64_str = f'{b64}'.split("'")[1]
    print(sys.getsizeof(b64_str))