import requests
import time


def register_api():
    headers = {
        "content-type": "application/json"
    }

    print("\n\n")

    print("-------------------------------------REGISTER IN API HIRE-GAME----------------------------------------")
    register_url = "https://hire-game.netsach.dev/api/v1.1/auth/register/"

    email = "alfredkuate@gmail.com"
    password1 = "alfred2000"
    password2 = "alfred2000"
    # email = input("Entrer votre adresse mail:")
    # password1 = input("Entrer votre mot de passe:")
    # password2 = input("Confirmer votre mot de passe:")
    data_register = {
        "email": email,
        "password1": password1,
        "password2": password2
    }
    print("\n\n")

    response = requests.post(register_url, json=data_register, headers=headers)

    if response.status_code == 201:
        data = response.json()
        token = data.get("token")
        uid = data.get("uid")
        email = data.get("email")
        print("Statut code:", response.status_code,
              " Enregistrement réussi. Token :", token)
        print("UID:", uid)
        print("Email:", email)
    else:
        print("Échec de l'enregistrement :", response.status_code)

    print(response.text)
  

# Connexion a l'API


def login_api():
    headers = {
        "Content-Type": "application/json"
    }

    login_url = "https://hire-game.netsach.dev/api/v1.1/auth/login/"
    print("\n\n")
    print("-------------------------------------LOGIN IN API HIRE-GAME----------------------------------------")

    email = "alfredkuate@gmail.com"
    password = "alfred2000"

    data_login = {
        "email": email,
        "password": password
    }
    print("\n")

    response = requests.post(login_url, json=data_login, headers=headers)

    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        uid = data.get("uid")
        email = data.get('email')
        print('CONNEXION REUSSIE:')
        print("------------------------------------------\n")
        print("Token :", token)
        print("------------------------------------------\n")
        print("Votre email:", email)
        print("-------------------------------------------\n")
        print("Votre UID(identifiant user):", uid)
        return token
    else:
        print("Échec de la connexion :", response.status_code)


# creation du job application
def create_job_application(session_token):
    url = "https://hire-game.netsach.dev/api/v1.1/job-application-request/"

    headers = {
        "Authorization": "Token " + session_token,
        "Content-Type": "application/json"
    }

    print("---------------------------------------------------------------\n")

    print("--------------------------------APPLICATION CREATED------------------------------------\n")

    email = "alfredkuate@gmail.com"
    first_name = "Alfred"
    last_name = "Kuate"

    data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name
    }
    data_array = {}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        data = response.json()
        application_id = data.get("uid")
        application_url = data.get("url")
        application_status = data.get("status")
        data_array = {
            "application_id": application_id,
            "application_url": application_url,
            "application_status": application_status,
        }
        print("Demande d'application créée.:", data_array)

        print("\n\n")

        print("--------------------------------CONFIRM APPLICATION------------------------------------\n")

        if application_url:
            # Timeout in case the confirmation isn't received
            timeout = 0

            while (timeout < 60):
                confirmation_url = get_confirmation_url(application_url, headers)
                print(confirmation_url["status"])
                # If the confirmation is complete, then break the loop
                if (confirmation_url["status"] == "COMPLETED"):
                    break
                timeout += 1

            if confirmation_url["status"] == "COMPLETED":
                confirm_application(confirmation_url['confirmation_url'], headers)
            else:
                print("Échec de confirmation de l'application")
        else:
            print("Échec de création de l'application")
    else:
        print("Échec de la création de la demande :", response.status_code)


# Recuperation de "confirmation_url"
def get_confirmation_url(application_url, headers):
    response = requests.get(application_url, headers=headers)
    array = {}
    if response.status_code == 200:
        data = response.json()
        confirmation_url = data.get("confirmation_url")
        status = data.get("status")
        array = {
            "confirmation_url": confirmation_url,
            "status": status
        }
        return array
    else:
        return None


# Confirmation de l'application
def confirm_application(confirmation_url, headers):

    boolean = {
        "confirmed": True
    }
    response = requests.patch(confirmation_url, headers=headers, json=boolean)
    if response.status_code == 200:
        print("-----------------------------------------------Application confirmée avec succès--------------------------------.")
    else:
        print("Échec de la confirmation de l'application :", response.status_code)


# Execution des differentes fonctions
register_api()
session_token = login_api()
create_job_application(session_token)
