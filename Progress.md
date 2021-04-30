## Features available
- data_dict(filename) 
    - for converting json to a list of dictionaries
    - for bus routes related stuff
- fare_dist(filename)
    - for converting csv file to a list of dictionaries
    - for bus fares

**Database**
Implemented
- lacking in foreign keys and shit

**Searching for nearest bus stop to a point**
- nearest_bus_stop(data, long, lat)
    - returns the dictionary of the nearest bus stop from a point

**Calculating travel fare between two points on a bus route**
- fare_dist(bus, startcode, endcode)
    - takes in bus service number, the starting bus code and ending bus code
    - returns the total distance travelled between the two bus stops and the direction of the bus(i.e 1 or 2)
- fares(bus,status, payment, dist, direction)
    - takes in the bus service number, status(i.e student, adult, etc.), payment type(card or cash), distance travelled and direction of route(i.e 1 or 2)
    - calculate the bus fare of the ride
    - returns the total bus fare in $

    
## Flask
**Nearest Bus Stop**
Status: Implemented

**Bus Fare Calculator**
Status: Implemented


## WIP features
**Current work**
- might implement `sort algo` in the function of searching for the nearest_bus_stop

**Abandoned for the moment**
- tyding up database

## Yet to be completed
- finding a place to put oop
- ER model & UML diagram
- error msgs in flask
- error msgs everywhere basicall
- dont lose out on doc strings

