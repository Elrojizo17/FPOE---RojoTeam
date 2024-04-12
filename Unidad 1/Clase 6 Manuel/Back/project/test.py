import requests

response = requests.get("http://localhost:8000")

#print(response.content)
data= {
    "Marca":"Prueba",
    "Sensor":"PruebaS",
    "CantBotones": 5,
    "DPI": 120000.0
}

response = requests.post("http://localhost:8000/v1/mouse",data)
print(response.status_code)
print(response.content)

