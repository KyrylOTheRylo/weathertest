import requests


def getweatherbycity(city: str = "Kiev", days: int = 3, url: str ="", headers: dict ={}):
    """

    :param city: you can write the city you want to check
    :param days: days forecasting
    :param url: api url base
    :param headers: headers with our info
    :return: response from an api
    """
    q = {"q": f"{city}", "days": days}
    resp = requests.request("GET", url, headers=headers, params=q)
    return resp


def get_exact_weather(info):
    """

    :param info: json file with weather data
    :return: dict with forecast weather per day
    """
    result = []
    place = info["location"]["name"]
    for x in info["forecast"]["forecastday"]:
        tmp = {"city": place,
               "date": x["date"],
               "min_temp": x["day"]["mintemp_c"],
               "avg_temp": x["day"]["avgtemp_c"],
               "max_temp": x["day"]["maxtemp_c"],
               "precip_mm": x["day"]["totalprecip_mm"],
               "totalshow_cm": x["day"]["totalsnow_cm"],
               "sunrise": x["astro"]["sunrise"],
               "sunset": x["astro"]["sunset"]}
        result.append(tmp)
    return result
