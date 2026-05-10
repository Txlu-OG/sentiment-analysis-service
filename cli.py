import requests
import sys

url = "http://localhost:5000/predict"

text = " ".join(sys.argv[1:])

response = requests.post(url, json={"text": text})
print(response.json())