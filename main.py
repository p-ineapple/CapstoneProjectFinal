from flask import Flask, render_template, request
from fileread import data_dict, fare_dict
import datastore
# from datastore import get_conc, insert_
import math
import sqlite3

"""
=================DICTIONARIES DUMP SECTION============================
"""
bus_routes = data_dict('bus_routes.json')
bus_services = data_dict('bus_services.json')
bus_stops = data_dict('bus_stops.json')

express = fare_dict('fare_data/fares-for-express-bus-services-effective-from-28-december-2019.csv')
feeder = fare_dict('fare_data/fares-for-feeder-bus-services-effective-from-28-december-2019.csv')
trunk = fare_dict('fare_data/fares-for-trunk-bus-services-effective-from-28-december-2019.csv')



"""
==================DATABASE DUMP SECTION=============================
"""
# conn = datastore.get_conn()
# cur = conn.cursor()
# datastore.insert_route(bus_routes)
# datastore.insert_service(bus_services)
# datastore.insert_stops(bus_stops)
# conn.commit()
# conn.close()

"""
==================FUNCTIONS DUMP SECTION=============================
"""
def nearest_bus_stop(lat, long):
    """
    """
    data = datastore.get_stops()
    dist_sort = []
    dist_data =[]
    for i in range(len(data)):
        lat_dist = float(lat) - data[i][-2]
        long_dist = float(long) - data[i][-1]
        value = long_dist**2 + lat_dist**2
        dist = value**0.5
        if i == 0:
            dist_data.append(dist)
            dist_sort.append(data[i])

        elif dist < dist_data[0]:
            dist_data.insert(0,dist)
            dist_sort.insert(0,data[i])

        else:
            for j in range(len(dist_data)-1):
                
                if dist_data [j] < dist <= dist_data[j+1]:
                    dist_data.insert(j+1,dist)
                    dist_sort.insert(j+1, data[j])
    return dist_sort[:5]


def fare_dist(bus, startcode, endcode):
    """
    """
    start_data  = datastore.get_stopsequence(bus, startcode)
    end_data  = datastore.get_stopsequence(bus, endcode)
    print( end_data, start_data)
    stopseq = [start_data[0][0], end_data[0][0], start_data[0][1]]
    all_stops = datastore.get_routes(bus, stopseq[-1], stopseq[0], stopseq[1])
    dist = 0
    for i in range(1, len(all_stops)):
        dist += all_stops[i][5]    
    return dist,start_data[0][1]


def fares(bus,status, payment, dist, direction):
    """
    """
    bus_type = datastore.get_bustype(bus, direction)
    bus_type = bus_type[0][0]
    info = [status,payment,'fare_per_ride']
    label = '_'.join(info)
    if bus_type == "TRUNK":
        data  = trunk
    else:
        data = express
    if bus_type == "FEEDER":
        data = feeder
        fare = data[0][label]
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
                if float(mini) <= dist <= float(maxi):
                    num = i
                    break
            fare = data[num][label]
    return fare


"""
===================FLASK CODE DUMP SECTION============================
"""

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/nearestbus')
def nearestbus():
    if "long" in request.args and "latt" in request.args:
        latt = request.args["latt"]
        long = request.args["long"]
        data = nearest_bus_stop(latt, long)
        return render_template('nearestbus.html',data=data)

@app.route('/fare')
def fare():
    if "busno" in request.args and "payment" in request.args and "status" in request.args and "start" in request.args and "end" in request.args:
        busno = request.args["busno"]
        status = request.args["status"]
        payment = request.args["payment"]
        start = request.args["start"]
        end = request.args["end"]

        dist, direction = fare_dist(busno, start, end)

        price = fares(busno,status, payment, dist, direction)
        if int(price) >= 100:
            price = str(price)
            price = price[:-2]+'.'+price[-2:]
        else:
            price = '0.'+str(price)

        return render_template('fare.html', busno=busno, payment=payment, status=status, start=start, end=end, price=price)


app.run('0.0.0.0')


#1. unpacking the json file( prob the routes first)✓
#2. creat sql data base to store the values
#searching for nearest bus stop to a point ✓
#find the bus
#use the 2 points find the distance
#use a speed to determine the time???
