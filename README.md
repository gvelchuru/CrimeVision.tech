# CrimeVision.Tech

This project is a proof-of-concept web page designed to allow users to easily examine historical crime data, predict future crime hotspots, and find safe spots to park their cars. 

We use the Seattle Police Database to create crime heatmaps, as well as a k-nearest neighbors classifier on the last 5 years to predict future crime hotstops. The green-hued areas represent the places where crimes have occured based on the Seattle Police Database dataset, whereas the blue-hued areas represent the areas where crimes could occur in the near future. The model, on test data, performs with over 95% accuracy. On completely unseen data, the model clearly finds clusters to predict future crime hotspots.
Further, we use the Google Maps Places API, and the Liberty Mutual Shine API to find parking areas, and parking meters, respectively. Red dots represent meters, while blue represent parking areas. 
Finally you can also see the travel route and the crime probablitites in the areas which could help you choose a different route.

### To run locally:

npm install

node index.js

go to localhost:3000
  
  
