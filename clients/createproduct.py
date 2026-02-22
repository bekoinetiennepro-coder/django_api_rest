import requests

endpoint = "http://localhost:8000/api/products/"

data={
    "name":"Product 2", 
    "description":"This is a description of Product 2",
    "price": 12000,
    "email": "test@example.com"
}

response = requests.post(endpoint, json=data)
print(response.json())
print(response.status_code)