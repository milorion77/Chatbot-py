import requests
import json


def enviarMensajeWhatsapp(data):  #todo data ingresa por parametros
    try:

        token = "EAAMAadkYL4UBOwF1LZB1sHRNq4HF94xKGSpEtJuulgNQwWbrf0m4iLRJVKoqYK4xcgw9uBXNFQdPDE7B6axjfnupZAnU3pwnDJB9Yw53TZA3arhbdLs5ZBuAQ1f3zBWUP0lsfrESuu7jve2ZBJ7jmRhzo7WQVZBE55pCiEsZByVohnZBOhv5M3lZBzq4bY7EO1bpv"

        api_url = "https://graph.facebook.com/v17.0/111084942093960/messages"

        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + token}

        response = requests.post(
            api_url, data=json.dumps(data), headers = headers)

        if response.status_code == 200:
            print("6")
            return True
        return False

    except Exception as exception:
        print(exception)
        return False
