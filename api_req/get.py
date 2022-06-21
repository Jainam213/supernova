import requests, json

headers = {
    'accept': 'text/plain',
}

mid = 'fea30235-7d5e-4d88-9ee2-116e2c5fc85e'

url = f"https://api2.spectre3d.io/Scan/{mid}"

response = requests.get(url, headers=headers)

dta = response.text
main = json.loads(dta)
print(response)
print(main["glbUrl"])
print(main["objUrl"])