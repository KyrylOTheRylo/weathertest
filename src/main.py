from requestapi import get_exact_weather, getweatherbycity
from mongo import create_db, open_collection, insert

HEADERS = {
    "X-RapidAPI-Key": "0187324a52msh0eaa900ff5d671dp18c951jsn4147fe93861d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
ADDRESS = "mongodb://127.0.0.1:27017"

if __name__ == "__main__":
    response = getweatherbycity(city="NY", days=6, url=url, headers=HEADERS)
    info = response.json()

    db = create_db("weather", ADDRESS)
    collection = open_collection(db, "forecast")
    for x in get_exact_weather(info):
        insert(collection, x)

    for document in collection.find():
        print(document)
