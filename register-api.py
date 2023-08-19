
import requests
import json

headers = {
  "content-type":"application/json"
}
register_url = "http://hire-game.netsach.dev/api/v1.1/auth/register/"

data_register = 
{
  "email": "a_kuatekuate@hetic.eu", 
  "password1": "alfred2000", 
  "password2": "alfred2000"
}

response = requests.post(register_url, json= data_register, headers= headers)
# print(requests.Response)
if response.status_code == 201:
    data = response.json()
    token = data.get("token")
    uid = data.get("uid")
    email = data.get("email")
    print("Statut code:", response.status_code, " Enregistrement réussi. Token :", token)
    print("UID:", uid)
    print("Email:", email)
else:
  print("Échec de l'enregistrement :", response.status_code)
print(response.text)  # Ajout de cette ligne pour afficher la réponse complète du serveur

