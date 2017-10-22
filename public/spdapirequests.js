function get_crimes_url(limit, offset) {
	url = "https://data.seattle.gov/resource/policereport.json?$limit="
	url += limit
	url += "&$offset="
	url += offset
	return url
}

function get_crimes(limit, offset, callback) {
	url = get_crimes_url(limit, offset)
    let options = {
      "url": url,
      "method": "GET",
      "processData": false
    }
    console.log("here")

    $.ajax(options).done((response)=>{
        success: callback(response)
    })
}