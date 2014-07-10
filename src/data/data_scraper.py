import requests

url = 'http://data.cityofnewyork.us/resource/h9gi-nx95.json'
r = requests.get(url)
collision_data = r.json()

# Returns an array of a [Date,Lat,Long] arrays for all collisions from a NYPD MV Collisions json file

def get_data(json_file):
    collision_array = []
    for collision in json_file:
        if get_date(collision) != None and get_latitude(collision) != None and get_longitude(collision) != None:
            try:
                collision_array.append([get_date(collision),get_latitude(collision),get_longitude(collision)])
            except:
                pass
    return collision_array

# Returns an array of Google Maps Lat/Long objects

def get_data(json_file):
    collision_array = []
    for collision in json_file:
        if get_date(collision) != None and get_latitude(collision) != None and get_longitude(collision) != None:
            try:
                collision_array.append([get_date(collision),get_latitude(collision),get_longitude(collision)])
            except:
                pass
    return collision_array

# Returns an array of Google Maps Lat/Long objects

def get_lat_long(json_file):
    collision_array = []
    for collision in json_file:
        if get_latitude(collision) != None and get_longitude(collision) != None:
            try:
                collision_array.append("new google.maps.LatLng("+get_latitude(collision)+" ,"+get_longitude(collision)+")")
            except:
                pass
    return collision_array

# Get methods for specific collision parameters

def get_date(collision):
    try:
        return collision['date'][0:10]
    except: 
        pass

def get_latitude(collision):
    try:
        return collision["location"]["latitude"]
    except:
        pass

def get_longitude(collision):
    try:
        return collision['location']['longitude']
    except:
        pass

# print get_lat_long(collision_data)
f = open('data', 'w')
collision_array = get_lat_long(collision_data)
collision_string = ', '.join(collision_array)
f.write(collision_string)
f.close()
