from urllib.request import urlopen, Request
import json

request = Request('https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/JS2YC415385101582?format=json')

cardict = {}
response_body = urlopen(request).read()
for i in json.loads(response_body)['Results']:
    cardict.update({i['Variable']: i['Value']})
    print(i['Variable'], i['Value'])
    print()

print(cardict)