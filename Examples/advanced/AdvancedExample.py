import requests
import jthon
from datetime import datetime, timezone

def event_time(time):
    time = time // 1000.0
    return ''.join(str(datetime.fromtimestamp(time, tz=timezone.utc))[:-6].split())

    
file = jthon.load('EarthquakeExample') #load the file into jthon
start = file.get('start').get('time')  #get something from the file
resp = requests.get(f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude=61.2140767&longitude=-149.8454911&maxradius=15&starttime={start}")
data = resp.json()
if data["metadata"]["count"] != 0:
    time_check = event_time(data['features'][0]['properties']['time'])
    if time_check not in str(start):
        for x in range(data["metadata"]["count"]):
            time = event_time(data['features'][x]['properties']['time'])
            if time not in file.get('items'):
                place = data['features'][x]['properties']['place']
                mag = data['features'][x]['properties']['mag']
                print(f'A magnitude {mag} at {place} reported at {time[-8:]}|{time[:10]}')
                file['items'][time] = place
                file.save()

        if len(file.get('items')) >= 1:
            file['start']['time'] = sorted(file.get('items'))[-1]
            file.save()
    else:
        print('no new items')
else:
    print('no new items')

    
results = file.find(value='Anchorage', exact=False, limit=3) #exact defaults to True, and limit defaults to all.
#search all values for a string, in this case we wanted 'contains' and not an exact value limited to 3 results.
print (f"previous results: {', '.join(str(item.value) for item in results)}") #itterate through the objects received and print the values.
