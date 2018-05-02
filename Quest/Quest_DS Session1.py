import json
from urllib.request import urlopen

html = urlopen("https://freegeoip.net/json/192.168.35.157")
data = json.loads(html.read())

print(data)

print({"IP":data['ip']})
print({"위도":data['latitude']})
print({"경도":data['longitude']})
