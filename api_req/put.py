import requests, json

headers = {
    'accept': 'text/plain',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

vid = './1.mp4'

files = {
    'file': open(vid, 'rb'),
    'scanQuality': (None, 'Full'),
    'featureSensitivity': (None, 'Normal'),
    'sampleOrdering': (None, 'Sequential'),
    'isObjectMaskingEnabled': (None, ''),
}

response = requests.post('https://api2.spectre3d.io/Scan', headers=headers, files=files)

dta = response.text
main = json.loads(dta)
print(response)
print(type(main))
print(main["id"]) 