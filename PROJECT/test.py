import requests

url = "https://language-translation.p.rapidapi.com/translateLanguage/detect-language"

querystring = {"text":"Hello"}

headers = {
    'x-rapidapi-key': "4b99efdab5mshdb0c8bd3b574635p16b3e8jsn57e7e6864ed5",
    'x-rapidapi-host': "language-translation.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
