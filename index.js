
const express = require('express')
const app = express()
const port = 3000
var path = require('path');

//app.get('/', (request, response) => {
//  response.send('Hello from Express!')
//})

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.use(express.static(path.join(__dirname, 'public')))

app.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})