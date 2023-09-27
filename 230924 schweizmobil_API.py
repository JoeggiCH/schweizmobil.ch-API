"""
This python script
- authenticates to schweizmobil.ch with a given username/password
- obtains the list of tracks
- per track finds the detail info
- determines the two opposite corners of a rectangle covering the via points
- prints all info into a CSV style format

Joerg Kummer 24. Sept 2023
"""

import requests
import json

pre = 'https://map.schweizmobil.ch'
session = requests.Session()
session.headers={}

# username / password for schweizmobil.ch
payload = json.dumps({
  "username": "",
  "password": ""
})
response = session.post(pre+'/api/4/login',data=payload)
#print (response.status_code)

response = session.get(pre+'/api/5/tracks')
tracks=response.json()

# output filename
f=open("tracks.csv",mode="w")

# CSV separator
s=';'
print ("id",s,"name",s,"time type",s,
       "length",s,"total up",s,"total down",s,
       "min elevation",s,"max elevation",s,"height diff",s,
       "walking time",s,"biking time",s,
       "userdate",s,"created at",s,"modified at",s,
       "imported",s,"original id",s, "public",s,"gps points",s,
       "velospeed",s,"filter name",s,"filter id",s,
       "South min",s,"West min",s,"North max",s,"East max",
       file=f)

for i in tracks:
    id=i['id']
    response = session.get(pre+'/api/4/tracks/'+str(id))
    track=response.json()
    props=track["properties"]

    # the coordinates are in the Swiss LV03 format
    # https://www.swisstopo.admin.ch/en/knowledge-facts/surveying-geodesy/reference-frames/local.html
    # LV03 measures the km distance from a reference point, south and west of Switzerland
    # i.e. a large west/east value means the point is more to the east
    # i.e. a large north/south value means the point is more to the north
    try:
        via=json.loads(props["via_points"])
        xmax=0; ymax=0
        xmin=1000000; ymin=1000000   
        for j in via:
            xmax=max(xmax,j[1])
            xmin=min(xmin,j[1])
            ymax=max(ymax,j[0])
            ymin=min(ymin,j[0])
    except:
        continue
        
    print (id,s,
           props["name"],s,
           props["timetype"],s,
           props["meta"]["length"],s,
           props["meta"]["totalup"],s,
           props["meta"]["totaldown"],s,
           props["meta"]["elemin"],s,
           props["meta"]["elemax"],s,
           props["meta"]["heightdiff"],s,
           props["meta"]["walking"],s,
           props["meta"]["biking"],s,
           props["userdate"],s,
           props["created_at"],s,
           props["modified_at"],s,
           props["imported"],s,
           props["original_id"],s,
           props["public"],s,
           props["gpspoints"],s,
           props["velospeed"],s,
           props["filter_name"],s,
           props["filterid"],s,
           xmin,s,ymin,s,xmax,s,ymax,
           file=f)
f.close()
print("done")
    

