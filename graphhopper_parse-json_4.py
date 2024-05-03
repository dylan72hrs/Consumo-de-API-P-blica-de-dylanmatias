import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."                          # ciudades de origen y destino
loc2 = "Baltimore, Maryland"
key = "082a3db8-90cd-472b-ad09-141581a7aff7"      # Replace with your Graphhopper API key

def geocoding (location, key):
    while location == "":
        location = input("Enter the location again: ")
        
    geocode_url = "https://graphhopper.com/api/1/geocode?" 
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code                               # parte 1 para arriba
    
    if json_status == 200 and len(json_data["hits"]) != 0:
        json_data = requests.get(url).json()

        json_data = requests.get(url).json()
        lat=(json_data["hits"][0]["point"]["lat"])
        lng=(json_data["hits"][0]["point"]["lng"])
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""
        
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""
        
        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)
    else:
        lat="null"
        lng="null"
        new_loc=location
        if json_status != 200:                                  # esta linea permite que si escribe algo al azar (slkdjf) muestre NULL NULL
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])   # permite que al usuario le muestre mensaje de error en la geocodificacion
    return json_status,lat,lng,new_loc
                                                             # parte 2 hacia arriba.py
while True:                                          # permite escribir al usuario las direcciones donde quieres ir
    loc1 = input("Starting Location: ")
    if loc1 == "quit" or loc1 == "q":                 # permite salir al usuario con (Q) o (QUIT)
        break
    orig = geocoding(loc1, key)
    print(orig)

    loc2 = input("Destination: ")
    if loc2 == "quit" or loc2 == "q":                # permite salir al usuario con (Q) o (QUIT)
        break
    dest = geocoding(loc2, key)
    print(dest)                                       # permite escribir al usuario las direcciones donde quieres ir
                                                       # DE ACA ARRIVA ES EL 3
                                                        # DE ACA ARRIbA ES EL 4 con muchos cambios a comparacion del 3    


























