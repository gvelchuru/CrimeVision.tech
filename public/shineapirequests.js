function measure(lat1, lon1, lat2, lon2){  // generally used geo measurement function
    var R = 6378.137; // Radius of earth in KM
    var dLat = lat2 * Math.PI / 180 - lat1 * Math.PI / 180;
    var dLon = lon2 * Math.PI / 180 - lon1 * Math.PI / 180;
    var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLon/2) * Math.sin(dLon/2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    var d = R * c;
    return d * 1000; // meters
}

//this is a frontend function but eventually it will query
//the backend before hitting the api. 

//def fetch_nearby(lat1, lng1): 
//    for (lat2, lng2) in LIST_OF_LATLNGS.keys(): 
//        if(get_dist(lat1, lng1, lat2, lng2) < 100): 
//            return LIST_OF_LATLNGS[(lat2, lng2)]
//    return False 
    
function get_meters_url(lat, lng) {
    url = "https://apis.solarialabs.com/shine/v1/parking-rules/meters?lat="
    url += lat
    url += "&long="+lng
    url += "&max-results=10&apikey=vyd6xVuOrpFCfkHRF6xETS9km7riggZe"
    return url
}    

function get_meters(lat, lng, callback) {
    // stored = fetch_nearby(lat, lng) 
    // if(stored) return stored
    url = get_meters_url(lat, lng)
    console.log(lat, lng)
    let options = {
      "url": url,
      "method": "GET",
      "processData": false
    }
    console.log("here")

    $.ajax(options).done((response)=>{
        success: callback(response)
    })
    //response = requests.get(url)
    // LIST_OF_LATLNGS[(lat, lng)] = response
    // return response.json()
} 
//url = "https://apis.solarialabs.com/shine/v1/parking-rules/meters?lat=47.6062&long=-122.3321&apikey=vyd6xVuOrpFCfkHRF6xETS9km7riggZe"
//url = get_meters(47.6062, -122.3321)
//response = requests.get(url)
//print(url, response.json(), response.status_code)