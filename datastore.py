import sqlite3
# conn = sqlite3.connect('capstone_project.db')
# c = conn.cursor()
# c.execute(

SQL = {
    'bus_routes_table':'''
    CREATE TABLE IF NOT EXISTS "bus_routes"(
        "ServiceNo" INTEGER,
        "Operator" TEXT,
        "Direction" INTEGER,
        "StopSequence" INTEGER,
        "BusStopCode" INTEGER,
        "Distance" INTEGER,
        "WD_FirstBus" INTEGER,
        "WD_LastBus" INTEGER,
        "SAT_FirstBus" INTEGER,
        "SAT_LastBus" INTEGER,
        "SUN_FirstBus" INTEGER,
        "SUN_LastBus" INTEGER,
        PRIMARY KEY ('ServiceNo','Direction','StopSequence'));
    ''',

    'bus_services_table':'''
    CREATE TABLE IF NOT EXISTS "bus_services"(
        "ServiceNo" INTEGER,
        "Operator" TEXT,
        "Direction" INTEGER,
        "Category" TEXT,
        "OriginCode" INTEGER,
        "DestinationCode" INTEGER,
        "AM_Peak_Freq" TEXT,
        "AM_Offpeak_Freq" TEXT,
        "PM_Peak_Freq" TEXT,
        "PM_Offpeak_Freq" TEXT,
        "LoopDesc" TEXT,
        PRIMARY KEY('ServiceNo','Direction','DestinationCode'));
    ''',

    'bus_stops_table':'''
    CREATE TABLE IF NOT EXISTS "bus_stops"(
        "BusStopCode" INTEGER,
        "RoadName" TEXT,
        "Description" TEXT,
        "Latitude" REAL,
        "Longitude" REAL,
        PRIMARY KEY(BusStopCode));
    ''',

    'insert_route':'''
    INSERT INTO bus_routes
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
    ''',

    'insert_service':'''
    INSERT INTO bus_services
    VALUES(?,?,?,?,?,?,?,?,?,?,?);
    ''',

    'insert_stops':'''
    INSERT INTO bus_stops
    VALUES(?,?,?,?,?);
    ''',

    'get_routes':'''
    SELECT * FROM bus_routes
    WHERE bus_routes.ServiceNo = ? 
    ''',

    'get_services':'''
    SELECT * FROM bus_routes
    WHERE bus_routes.ServiceNo = ? 
    ''',

    'get_stops':'''
    SELECT * FROM bus_stops
    WHERE bus_stops.BusStopCode = ? 
    ''',
    }



def get_conn():
    conn = sqlite3.connect('capstone.db')
    return conn
    
conn = get_conn()
cur = conn.cursor()

def insert_route(data):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(SQL['bus_routes_table']);
    for entry in data:
        values = entry.values()
        cur.execute(SQL['insert_route'],list(values))

def insert_service(data):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(SQL['bus_services_table']);
    for entry in data:
        values = entry.values()
        cur.execute(SQL['insert_service'],list(values))

def insert_stops(data):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(SQL['bus_stops_table']);
    for entry in data:
        values = entry.values()
        cur.execute(SQL['insert_stops'],list(values))

# def get_routes(data)
conn.commit()
conn.close()
