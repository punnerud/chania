import requests

response = requests.get(
    #'https://chania.3pi-telematics.com/en/api/getRouteDetailPerRoute/1391', #Rute
    'https://chania.3pi-telematics.com/el/api/getBusLocation/1391/', #Busslokasjon
    params=[('a', '1')], verify=False,
headers={'Accept': '*/*',
   'Accept-Encoding': 'gzip, '
   'deflate',
   'Accept-Language': 'en-us',
   'Connection': 'keep-alive',
   'Cookie': 'PHPSESSID=djt6gdbi1o771nvatcpuc269h0',
   'User-Agent': 'transit/9 '
   'CFNetwork/901.1 '
   'Darwin/17.6.0'}
)

print(response.text)



