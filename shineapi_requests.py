import requests
import math

def get_dist(lat1, lng1, lat2, lng2):
    R = 6378.137
    d_lat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    d_lng = lng2 * math.pi / 180 - lng1 * math.pi / 180
    a = math.sin(d_lat/2) ** 2 + math.cos(lat1 * math.pi /180) *
        math.cos(lat2 * math.pi / 180) * math.sin(d_lng / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d * 1000

def fetch_nearby(lat1, lng1): 
    for (lat2, lng2) in LIST_OF_LATLNGS.keys(): 
        if(get_dist(lat1, lng1, lat2, lng2) < 100): 
            return LIST_OF_LATLNGS[(lat2, lng2)]
    return False 
    
def get_meters_url(lat, lng):
    url = "https://apis.solarialabs.com/shine/v1/parking-rules/meters?lat="
    url += str(lat)
    url += "&long="+str(lng)
    url += "&apikey=vyd6xVuOrpFCfkHRF6xETS9km7riggZe"
    return url
    
def get_meters(lat, lng): 
    #stored = fetch_nearby(lat, lng) 
    #if(stored) return stored
    url = get_meters_url(lat, lng)
    response = requests.get(url)
    #LIST_OF_LATLNGS[(lat, lng)] = response
    return response.json()
    
#url = "https://apis.solarialabs.com/shine/v1/parking-rules/meters?lat=47.6062&long=-122.3321&apikey=vyd6xVuOrpFCfkHRF6xETS9km7riggZe"
#url = get_meters(47.6062, -122.3321)
#response = requests.get(url)
#print(url, response.json(), response.status_code)