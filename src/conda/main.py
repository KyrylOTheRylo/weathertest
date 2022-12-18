from requestapi import get_exact_weather, getweatherbycity
from mongo import create_db, open_collection, insert, insert_many
import redis
from bson.json_util import dumps
import json
import time
import random

HEADERS = {
    "X-RapidAPI-Key": "0187324a52msh0eaa900ff5d671dp18c951jsn4147fe93861d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
ADDRESS = "mongodb://citizix:S3cret@weathertest-mongodb-1:27017/"
USERNAME = ""
PASS = ""
CITY1 = ["London", "Ontario", "Paris", "NY"]

if __name__ == "__main__":

    db = create_db("weather", ADDRESS)
    with redis.Redis(host="weathertest-rdb-1", port=6379) as rdb:
        c = 0
        rdb.set("timer", c)
        tmdb = open_collection(db, "timer")
        collection = open_collection(db, "forecast")
        tmdb.insert_one({"timer": rdb.get("timer")})
        tmdb.update_one({}, {"$set": {'timer': rdb.get("timer")}})
        while True:
            print("--------------------------------------------")

            for city in CITY1:
                response = getweatherbycity(city=city, days=6, url=url, headers=HEADERS)
                info = response.json()
                for x in (get_exact_weather(info)):
                    rdb.set(name=str(x["_id"]["city"] + ":" + x["_id"]["date"]), value=dumps(x))

            time.sleep(60)
            tmp = []
            for key in rdb.keys("*"):
                if not key.decode() == "timer":
                    print((rdb.get(key)), str(key))
                    tmp.append(json.loads(rdb.get(key)))
            rdb.flushdb()
            insert_many(collection, tmp)
            c += 1
            rdb.set("timer", c)
            if random.randint(0, 5) == 4:
                tmdb.update_one({}, {"$set": {'timer': rdb.get("timer")}})
