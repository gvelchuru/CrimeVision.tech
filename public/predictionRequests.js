function get_predictions(callback) {
  //file = JSON.parse()
	//url = get_crimes_url(limit, offset)
    let options = {
      "url": "2018_keylist.txt",
      "dataType": "json",
      "method": "GET",
      "processData": false
    }
    console.log("here for the file reading ;)")

    $.ajax(options).done((response)=>{
        success: callback(response)
    })
}