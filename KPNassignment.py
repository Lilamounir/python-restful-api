'''
Created on Mar 2, 2016

@author: Lila
'''

import csv
import json
import requests

csvfile = open('contact_application_data - Sheet1.csv', 'r')
f = open('contact_application_data - Sheet1.json', 'w')

fieldnames = ("firstname","lastname","street","zip","city","image")
reader = csv.DictReader(csvfile)
for row in reader:
    jsonfile = json.dumps( [ row for row in reader ] )
    f.write('\n')

with open('timeline2.json', 'w') as outfile:
    json.dump(jsonfile, outfile)

url = 'https://docs.google.com/spreadsheets/d/1KdK_9vltr9Yu6tyAfenlDoITeAkdczyCf9r2UCwe0AE/edit?usp=sharing_eid&ts=56dc88be'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
print jsonfile

