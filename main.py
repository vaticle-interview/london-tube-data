import os
import mysql.connector
import json
from root.nested.jsonRead import station


f = open('train-network.json')
data = json.load(f)
  
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Swimming-94"
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE mydatabase")



for station in data['stations']:
    print(station)
    name = station.get("name", None)
    ID = station.get("id", None)
    longitude = station.get("longitude", None)
    latitude = station.get("latitude")
    
    cursor.execute("INSERT INTO mydatabase.station (name,    id,    longitude,    latitude) VALUES (%s,    %s,    %s,    %s)", (name,    ID,    longitude, latitude))

mydb.commit()
mydb.close()
# Closing file
f.close()



print(mydb)