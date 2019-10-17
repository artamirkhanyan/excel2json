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


def open_csv(to_read):
	csv_data_df = pd.read_csv(to_read, header=None, encoding="latin1")
	alldata = []
	for index, row in csv_data_df.iterrows():
		alldata.append(list(row))
	return (alldata)


def open_excel(to_read):
	alldata = []
	try:
		wb = xlrd.open_workbook(to_read, logfile=open(os.devnull, 'w'))
	except UnicodeDecodeError:
		wb = xlrd.open_workbook(to_read, logfile=open(os.devnull, 'w'), encoding_override="latin1")

	xl = pd.read_excel(wb, engine='xlrd',header=None)
	xl.replace(np.nan, '', inplace=True)

	for index, row in xl.iterrows():
		alldata.append(list(row))
	return alldata


output_list = []

if file.lower().endswith(('.xlsx', '.xls')):
	output_list = open_excel(file)
elif file.lower().endswith('.csv'):
	output_list = open_csv(file)
else:
	print(json.dumps({"error":True, "msg": "File format is not supported."}))
	sys.exit()


json_data = json.dumps({"error":False, "data": output_list})
print(json_data)
#print ((time.time()- start))
