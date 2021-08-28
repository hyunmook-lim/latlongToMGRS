import requests
import pprint


location = '숭의1.3동 421-17 숭의공구상가입구'

URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=<AIzaSyCveorDUHsBJ4TyiQ0EyYMSHzw_xPwiZk0>' '&sensor=false&language=ko&address={}'.format(location)

response = requests.get(URL)

data = response.json()

pprint.pprint(data)
'''
lat = data['results'][0]['geometry']['location']['lat']
lng = data['results'][0]['geometry']['location']['lng']

pprint.pprint(lat)
pprint.pprint(lng)
'''
