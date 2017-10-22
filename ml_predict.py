import json
from collections import OrderedDict
import numpy as np
import joblib


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


classifier = joblib.load('model.pkl')
min_lat = 47.4
max_lat = 47.8
min_long = -122.5
max_long = -122.2

year = 2018
iterate = .001
lat_long_dict = OrderedDict()
for lat in np.arange(min_lat, max_lat, iterate):
    for long in np.arange(min_long, max_long, iterate):
            for month in range(1, 12 + 1):
                lat_long_dict[truncate(lat, 3), truncate(long, 3), year, month] = 0
keyList = list(lat_long_dict.keys())
predicted = classifier.predict(keyList).tolist()
json.dump(keyList, open('2018_keyList.txt', 'w'))
json.dump(predicted, open('2018_predict.txt', 'w'))