# Python 3
import urllib.request, json 
import Crime
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def get_crime_information():
	cl = []
	with urllib.request.urlopen("https://data.seattle.gov/resource/policereport.json?$limit=5000") as url:
	    data = json.loads(url.read().decode())
	    count = 0
	    for offense in data:
	    	count += 1
	    	crime = Crime.Crime(offense)
	    	cl.append(crime.get_location())	
	    return np.array(cl)


def main():
	crime_list = get_crime_information() # X
	x = np.array(crime_list)
	#plt.plot(x)
	#plt.show()
	print(len(x))

	y = savgol_filter(x, 51, 2)
	print(y)
	

if __name__ == '__main__':
	main()