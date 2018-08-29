import requests, json, sqlite3, time
conn = sqlite3.connect('db.db')
c = conn.cursor()

unixnow = int(time.time())

response = requests.get(
    #'https://chania.3pi-telematics.com/en/api/getRouteDetailPerRoute/1391', #Rute
    'https://chania.3pi-telematics.com/el/api/getBusLocation/1391/', #Busslokasjon
    params=[('a', '1')], verify=False,
headers={'Accept': '*/*',
   'Accept-Encoding': 'gzip, '
   'deflate',
   'Accept-Language': 'en-us',
   'Connection': 'keep-alive',
   #s'Cookie': 'PHPSESSID=djt6gdbi1o771nvatcpuc269h0',
   'User-Agent': 'transit/9 '
   'CFNetwork/901.1 '
   'Darwin/17.6.0'}
)

r = json.loads(response.text)
for i in r:
	c.execute("insert INTO bus (veh, lat, lng, route, unixnow) VALUES (?,?,?,?,?)",(int(i["VEH_NO"]),float(i["CS_LAT"]),float(i["CS_LNG"]),int(i["ROUTE_CODE"]),unixnow))
    #print("Veh:",i["VEH_NO"])
    #print("CS_LAT:",i["CS_LAT"])
    #print("CS_LNG:",i["CS_LNG"])
    #print("ROUTE_CODE:",i["ROUTE_CODE"])
    #print("")
conn.commit()
conn.close()