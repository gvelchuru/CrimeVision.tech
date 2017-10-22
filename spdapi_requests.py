# Python 3
import urllib.request, json 
import Crime
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import pymesh

def get_crime_information():
	cl = []
	with urllib.request.urlopen("https://data.seattle.gov/resource/policereport.json") as url:
	    data = json.loads(url.read().decode())
	    count = 0
	    for offense in data:
	    	count += 1
	    	crime = Crime.Crime(offense)
	    	cl.append(crime.get_location())	
	    return np.array(cl)


def main():
	#crime_list = get_crime_information()
	#print(crime_list[:10])
	#clf = MultinomialNB()
	X = np.random.randint(5, size=(6, 100))
	y = np.array([1, 2, 3, 4, 5, 6])
	print(X)
	print(y)
	clf = MultinomialNB()
	print(clf)
	clf.fit(X,y)
	x2 = clf.predict(X[2:3])
	print(x2)
	#clf.fit(crime_list, crime_list[::10])

if __name__ == '__main__':
	main()