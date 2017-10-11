import requests
r = requests.get('api.civicapps.org/parks')
r = requests.get('http://api.civicapps.org/parks')
r.text
r = requests.ge'http://api.civicapps.org/business-licenses/')
r = requests.get('http://api.civicapps.org/business-licenses/')
r
r.json
d = r.json()
d
len(d)
d.keys()[0]
[k for k in d.keys()]
len(d['results'])
d = requests.get('http://api.civicapps.org/business-licenses/?from=2011-03-01&to=2011-05-01').json['results']
d = requests.get('http://api.civicapps.org/business-licenses/?from=2011-03-01&to=2011-05-01').json()['results']
d = requests.get('http://api.civicapps.org/business-licenses/?from=2000-01-01&to=2017-10-01').json()['results']
r = requests.get('http://api.civicapps.org/business-licenses/?from=2011-01-01&to=2017-01-01')
js = r.json()
len(js['results'])
r = requests.get('http://api.civicapps.org/business-licenses/?from=2011-01-01&to=2017-09-30')
js = r.json()
len(js['results'])
import pandas as pd
df = pd.io.json.json_normalize(js)
df.columns
df = pd.io.json.json_normalize(js['results'])
df
df.to_csv('business_permits.csv')
hist
hist -o 'business_permits.py'
ls
ls business_permits.py
hist --help
hist -h
help(hist)
hist --help
hist?
%help history
%history --help
%history?
hist -f 'buisiness_permits.py'
