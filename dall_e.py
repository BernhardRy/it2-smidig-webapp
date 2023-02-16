import requests
url = "https://api.openai.com/v1/images/generations"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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",
}   
data = {
  "prompt": "The IT-class going to lunch painted by Munch",
  "n": 2,
  "size": "1024x1024"
}
response = requests.post(url, headers=headers, json=data)
data = response.json()
print(data)