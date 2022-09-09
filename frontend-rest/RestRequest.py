import json
import requests


class RestRequests():
    def __init__(self, **kwargs):
        super(RestRequests, self).__init__(**kwargs)

    #Este será o método genérico de requisição
    def req(self, type, route, params):
        api_url = f"http://localhost:5000/api/{route}"
        jsonData = {
            "params": params,
        }
        response = {}
        if(type == "POST"):
            response = requests.post(api_url, json=jsonData).json()
        
        if(type == "GET"):
            response = requests.get(api_url, json=jsonData).json()
            print(response)

        if(type == "PUT"):
            response = requests.put(api_url, json=jsonData).json()
        return response