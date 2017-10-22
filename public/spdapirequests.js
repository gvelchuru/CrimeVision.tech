function get_crimes_url() {
	url = "https://data.seattle.gov/resource/policereport.json?$limit=50000"
	return url
}

function get_crimes(callback) {
	url = get_crimes_url()
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