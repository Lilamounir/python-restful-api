import csv
import requests

r = requests.get('https://docs.google.com/spreadsheets/d/1KdK_9vltr9Yu6tyAfenlDoITeAkdczyCf9r2UCwe0AE/pub?gid=266233705&single=true&output=csv') 
data = r.text

reader = csv.reader(data.splitlines(), delimiter=',')
for row in reader:
    print row

