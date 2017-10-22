import csv
import random
from collections import OrderedDict

import joblib
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# response_dict = json.load(open('initial_response_data.json'))
# print('kurwa')
# with urllib.request.urlopen('https://data.seattle.gov/resource/policereport.json', timeout=999999999) as url:
#     data = json.loads(url.read().decode())
# df = pd.read_json('https://data.seattle.gov/resource/policereport.json')

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

min_lat = 47.4
max_lat = 47.8
min_long = -122.5
max_long = -122.2

min_year = 2015
max_year = 2017

iterate = .001
lat_long_dict = OrderedDict()
for lat in np.arange(min_lat, max_lat, iterate):
    for long in np.arange(min_long, max_long, iterate):
        for year in range(min_year, max_year + 1):
            for month in range(1, 12 + 1):
                lat_long_dict[truncate(lat, 3), truncate(long, 3), year, month] = 0

# for lat in np.arange(min_lat, max_lat, iterate):
#     for long in np.arange(min_long, max_long, iterate):
#             for month in range(1, 12 + 1):
#                 lat_long_dict[truncate(lat, 3), truncate(long, 3), month] = 0



with open('Seattle_Police_Department_Police_Report_Incident.csv') as report_csv:
    # out_dict = []
    keys = []
    for index, row in enumerate(csv.reader(report_csv)):
        if index == 0:
            keys = row
        else:
            row_dict = {}
            for index, key in enumerate(keys):
                row_dict[key] = row[index]
            # out_dict.append(row_dict)
            latitude = truncate(float(row_dict['Latitude']), 3)
            longitude = truncate(float(row_dict['Longitude']), 3)
            year = int(row_dict['Year'])
            month = int(row_dict['Month'])
            if year in range(min_year, max_year + 1):
                lat_long_dict[latitude, longitude, year, month] += 1
index = 0
key_list = list(lat_long_dict.keys())
while True:
    if index == (int(1.5 * 2872800) - int(1.5 * 3000)):
        break
    else:
        i = random.randint(0, len(key_list) - 1)
        key = key_list[i]
        if key == 0:
            index += 1
            lat_long_dict.pop(key)
            key_list.pop(i)

# for crime in out_dict:
#     lat = float(crime['Latitude'])
#     long = float(crime['Longitude'])
#     if not min_lat:
#         min_lat = lat
#         max_lat = lat
#         min_long = long
#         max_long = long
#     else:
#         min_lat = min([min_lat, lat])
#         max_lat = max([max_lat, lat])
#         min_long = min([min_long, long])
#         max_long = max([max_long, long])
# print(min_lat)
# print(max_lat)
# print(min_long)
# print(max_long)
# json.dump(out_dict, open('initial_response_data.json', 'w'))


# for crime in out_dict:
#     year = float(crime['Year'])
#     if not min_year:
#         min_year = year
#         max_year = year
#     else:
#         min_year = min([min_year, year])
#         max_year = max([max_year, year])
# print(min_year)
# print(max_year)



# json.dump(lat_long_list, open('lat_long_list.txt', 'w'))

# lat_long_list = json.load(open('lat_long_list.txt'))
# data = [0 for _ in lat_long_list]
# for index, lat_long in enumerate(lat_long_list):
#     for crime in out_dict:
#         latitude = truncate(float(crime['Latitude']), 3)
#         longitude = truncate(float(crime['Longitude']), 3)
#         month = float(crime['Month'])
#         year = float(crime['Year'])
#         if latitude == lat_long[0] and longitude == lat_long[1] and year == lat_long[2] and month == lat_long[3]:
#             data[index] += 1

print('Training...')
# classifier = KNeighborsClassifier(n_jobs=-1)
classifier = KNeighborsClassifier(n_jobs=-1)
# classifier = autosklearn.classification.AutoSklearnClassifier()
data = list(lat_long_dict.keys())
target = list(lat_long_dict.values())
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.1)
classifier.fit(X_train, y_train)
joblib.dump(classifier, 'model.pkl')
out_file = open('out_file.txt', 'w')
predicted = classifier.predict(X_test)
out_file.write(metrics.classification_report(y_test, predicted))


