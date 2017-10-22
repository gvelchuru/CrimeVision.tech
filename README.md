# CrimeVision.Tech

This project is a proof-of-concept web page designed to allow users to easily examine historical crime data, predict future crime hotspots, and find safe spots to park their cars. 

We use the Seattle Police Database to create crime heatmaps, as well as (expand about ML). The green-hued areas represent the places where crimes have occured based on the Seattle Police Database dataset, whereas the blue-hued areas represent the areas where crimes could occur in the near future. The predictions are based on our model, which help us tell the areas with an accuracy of over 95%.
Further, we use the Google Maps Places API, and the Liberty Mutual Shine API to find parking areas, and parking meters, respectively. Red dots represent meters, while blue represent parking areas. 
Finally you can also see the travel route and the crime probablitites in the areas which could help you choose a different route.

### To run locally:

npm install

node index.js

go to localhost:3000
  
  
