#!/usr/bin/env python

import os
import sys
import xlrd
import pandas as pd
#import time
import json
import numpy as np

#start = time.time()

try:
	file = sys.argv[1]
except IndexError:
	print(json.dumps({"error":True, "msg": "File not provided."}))
	sys.exit()

if not os.path.isfile(file):
	print(json.dumps({"error":True, "msg": "File not found."}))
	sys.exit()

try:
	wb = xlrd.open_workbook(file, logfile=open(os.devnull, 'w'))
except UnicodeDecodeError:
	wb = xlrd.open_workbook(file, logfile=open(os.devnull, 'w'), encoding_override="latin1")


xl = pd.read_excel(wb, engine='xlrd',header=None)
xl.replace(np.nan, '', inplace=True)


alldata = []
for index, row in xl.iterrows():
	alldata.append(list(row))


json_data = json.dumps({"error":False, "data": alldata})
print(json_data)

#print ((time.time()- start))
