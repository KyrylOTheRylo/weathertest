from requestapi import get_exact_weather, getweatherbycity

HEADERS = {
    "X-RapidAPI-Key": "0187324a52msh0eaa900ff5d671dp18c951jsn4147fe93861d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

if __name__ == "__main__":
    response = getweatherbycity(city="Paris", days=6, url=url, headers=HEADERS)
    info = response.json()

    for x in get_exact_weather(info):
        print(x)
