import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q": "G2J", "days": "3"}

headers = {
    "X-RapidAPI-Key": "0187324a52msh0eaa900ff5d671dp18c951jsn4147fe93861d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
