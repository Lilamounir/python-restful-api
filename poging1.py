import pandas as pd
import csv
import json

data = pd.read_csv('https://docs.google.com/spreadsheets/d/1KdK_9vltr9Yu6tyAfenlDoITeAkdczyCf9r2UCwe0AE/pub?gid=266233705&single=true&output=csv')
data.to_csv('out.csv')

#print data
csvfile = open('out.csv', 'r')
f = open('out.json', 'w')
fieldnames = ('firstname', 'lastname', 'street', 'zip', 'city', 'image')
reader = csv.DictReader(csvfile)
for row in reader:
    jsonfile = json.dumps( [ row for row in reader ] )
    f.write('\n')

with open('out.json', 'w') as outfile:
    json.dump(jsonfile, outfile)
    
