import requests
from datetime import datetime

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
data_hoje = datetime.now().strftime("%Y-%m-%d")

headers = {
    "X-RapidAPI-Key": "3276157ce3msh8213e9a3b3118f4p16c026jsn9981bbb233d7",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

params = {
    "date": data_hoje
}

response = requests.get(url, headers=headers, params=params)

print("Status Code:", response.status_code)
print("Resposta da API:")
print(response.text)