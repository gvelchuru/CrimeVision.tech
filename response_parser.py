import csv
import json

import joblib
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

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


with open('Seattle_Police_Department_Police_Report_Incident.csv') as report_csv:
    out_dict = []
    keys = []
    for index, row in enumerate(csv.reader(report_csv)):
        if index == 0:
            keys = row
        else:
            row_dict = {}
            for index, key in enumerate(keys):
                row_dict[key] = row[index]
            out_dict.append(row_dict)
min_lat = 47.4
max_lat = 47.8
min_long = -122.4
max_long = -122.2
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

min_year = 1990
max_year = 2017
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


iterate = .001
lat_long_list = []
for lat in np.arange(min_lat, max_lat, iterate):
    for long in np.arange(min_long, max_long, iterate):
        for year in range(min_year, max_year):
            for month in range(1, 12):
                lat_long_list.append([lat, long, year, month])
# json.dump(lat_long_list, open('lat_long_list.txt', 'w'))

# lat_long_list = json.load(open('lat_long_list.txt'))
data = [0 for _ in lat_long_list]
for index, lat_long in enumerate(lat_long_list):
    for crime in out_dict:
        latitude = truncate(float(crime['Latitude']), 3)
        longitude = truncate(float(crime['Longitude']), 3)
        month = float(crime['Month'])
        year = float(crime['Year'])
        if latitude == lat_long[0] and longitude == lat_long[1] and year == lat_long[2] and month == lat_long[3]:
            data[index] += 1

print('Training...')
classifier = KNeighborsClassifier(n_jobs=-1)
classifier.fit(lat_long_list, data)
joblib.dump(classifier, 'model.pkl')



