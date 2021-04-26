from flask import Flask, render_template, request
from fileread import data_dict, fare_dict
import datastore
# from datastore import get_conc, insert_
import math
import sqlite3

bus_routes = data_dict('bus_routes.json')
bus_services = data_dict('bus_services.json')
bus_stops = data_dict('bus_stops.json')

express = fare_dict('fare_data/fares-for-express-bus-services-effective-from-28-december-2019.csv')
feeder = fare_dict('fare_data/fares-for-feeder-bus-services-effective-from-28-december-2019.csv')
trunk = fare_dict('fare_data/fares-for-trunk-bus-services-effective-from-28-december-2019.csv')

conn = datastore.get_conn()
cur = conn.cursor()
datastore.insert_route(bus_routes)
datastore.insert_service(bus_services)
datastore.insert_stops(bus_stops)
conn.commit()
conn.close()



def nearest_bus_stop(data, long, lat):
    #1° ≈ 111km
    for i in range(len(data)):
        long_dist = float(long) - data[i]['longtitude']
        lat_dist = float(lat) - data[i]['lattitude']
        dist = math.sqrt(long_dist**2 - lat_dist**2)
        if i == 0:
            shortest = dist
            bus_stop = i
        elif dist < shortest:
            shortest = dist
            bus_stop = i
    return data[bus_stop]

# def fare_dist(data, bus, startcode, endcode, direction):
    # found = False
    # i = 0
    # while not found:
    #     if data[i]['BusStopCode'] == startcode:
    #         index = i
    #         found = True
    
    conn = datastore.get_conn()
    cur = conn.cursor()

    datastore.get_routes()
    conn.commit()
    conn.close()
    

def fares(data, bus_type, human, payment, dist=None):
    info = [human,payment,'fare_per_ride']
    label = '_'.join(name)
    if bus_type == "feeder":
        fare = data[label]
    else:
        if dist < 3.2:
            fare = data[0][label]
        elif dist > 40.2:
            fare = data[0][label]
        else:
            for i in range(1, len(data)-1):
                dist_limit = data[i]['distance'].split(' ')
                mini = dist_limit[0]
                maxi = dist_limit[-2]
                if mini <= dist <= maxi:
                    num = i
                    break
            fare = data[num][label]
    return fare


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('test.html')

app.run('0.0.0.0')


#1. unpacking the json file( prob the routes first)✓
#2. creat sql data base to store the values
#searching for nearest bus stop to a point ✓
#find the bus
#use the 2 points find the distance
#use a speed to determine the time???
