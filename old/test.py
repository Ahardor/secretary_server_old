import requests

d = {"a" : "b"}
a = requests.post("http://127.0.0.1:8000", json=d)

print(a.json())