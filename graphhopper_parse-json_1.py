import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "082a3db8-90cd-472b-ad09-141581a7aff7"      # Replace with your Graphhopper API key

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})
replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print(json_data)

