# Python 3
import urllib.request, json 
import Crime

def get_crime_information():
	with urllib.request.urlopen("https://data.seattle.gov/resource/policereport.json") as url:
	    data = json.loads(url.read().decode())
	    count = 0
	    for offense in data:
	    	count += 1
	    	crime = Crime.Crime(offense)
	    	print("Summarized Offense Description: " + crime.description + " Started at: " + crime.start_time + " Latitude: " + crime.lat + ", Longitude: " + crime.lng)

def main():
	get_crime_information()

if __name__ == '__main__':
	main()