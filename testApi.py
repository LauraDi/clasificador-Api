import requests

review = {"entrada": "Viva amlo"}
resp = requests.post("http://localhost:8000/clasification", json=review)

print(resp.content)
