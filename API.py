import requests
import base64
import numpy
import time

url = 'https://api31-3r4z.vercel.app/rest/'
response = requests.get(url)
print(response)
headers = {
    'Content-Type': 'application/json'
}
# data = {
#     "pk": 66,
#     "longitude": 1231.34,
#     "latitude": 123.455,
#     "images": f"{base64.encodebytes(image.tobytes())}",
#     "is_accident": True,
#     "is_fire": True
# }
# print(base64.encodebytes(image.tobytes()))
times = []
for i in range(20):
    response = requests.get(url)
    print(response.status_code)

