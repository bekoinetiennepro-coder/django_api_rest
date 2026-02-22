import requests

endpoint = "http://localhost:8000/api/products/1/"

data={
    "name":"Product 2", 
    "description":"This is a description of Product 2",
    "price": 12000,
    "email": "test@example.com"
}

response = requests.get(endpoint)
print(response.json())
print(response.status_code)