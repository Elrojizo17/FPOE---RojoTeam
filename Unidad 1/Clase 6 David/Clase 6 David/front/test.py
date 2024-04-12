import requests

response = requests.get("http://localhost:8000")

print(response)

data = {
    "marca": "Yamaha",
    "cilindraje": 125,
    "modelo": 95,
    "color": "Rojo"
}

response = requests.post("http://localhost:8000/v1/moto", data=data)

print(response.status_code)

print(response.content)