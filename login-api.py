import requests


login_url = "http://hire-game.netsach.dev/api/v1.1/login"

data_login = {
    "email": "alfredkuate55@gmail.com",
    "password": "alfred2000"
}

response = requests.post(login_url, json=data_login)

if response.status_code == 200:
    data = response.json()
    token = data.get("token")
    print("Connexion réussie. Token :", token)
else:
    print("Échec de la connexion :", response.status_code)
