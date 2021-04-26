## Features available
- data_dict(filename) 
    - for converting json to a list of dictionaries
    - for bus routes related stuff
- fare_dist(filename)
    - for converting csv file to a list of dictionaries
    - for bus fares

**Database**
Implemented (but not checked)

**Searching for nearest bus stop to a point**
- nearest_bus_stop(data, long, lat)
    - returns the dictionary of the nearest bus stop from a point

**Calculating travel fare between two points on a bus route**
- fares(data, bus_type, human, payment, dist= None)
    - calculate the bus fare of the ride

    
## Flask
**Nearest Bus Stop**

Request Information
- bus number
- route
- human status
- payment type


## WIP features
**Current work**
- working on "calculating bus fare"
- things missing: `calculating distance`

**Abandoned for the moment**
- flask page