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
    print("=================================================")                                # permite que MUESTRE que APÍ STATUS  SEA CORRECTO Y QUE LLEGA AL IGUAL QUE LA URL                                  
    if orig[0] == 200 and dest[0] == 200:                      
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key":key}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print("Routing API Status: " + str(paths_status) + "\nRouting API URL:\n" + paths_url)  # permite que MUESTRE que APÍ STATUS  SEA CORRECTO Y QUE LLEGA AL IGUAL QUE LA URL
        print("=================================================")
        print("Directions from " + orig[3] + " to " + dest[3])                                 # permite que MUESTRE LA DURACION Y DISTANCIA DEL VIAJE
        print("=================================================")
        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"])/1000/1.61                        # permite Calcular la distancia en miles que es metros y KM que es kilometros
            km = (paths_data["paths"][0]["distance"])/1000                               # permite Calcular la distancia en miles que es metros y KM que es kilometros
            sec = int(paths_data["paths"][0]["time"]/1000%60)                             # permite los segundos que tardaras
            min = int(paths_data["paths"][0]["time"]/1000/60%60)                          # permite los minutos que tardaras
            hr = int(paths_data["paths"][0]["time"]/1000/60/60)                            # permite los horas que tardaras
            print("Distance Traveled: {0:.1f} miles / {1:.1f} km".format(miles, km))      # este codigo permite que muestre como resultado de los destinos que muestre los kilometros y metros de distancia
            print("Trip Duration: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))          # Este imprime como resultado todos las MINUTOS,SEGUNDOS,HORAS para mostrarle al usuario sobre su viaje
            print("=================================================")                           # permite que MUESTRE LA DURACION Y DISTANCIA DEL VIAJE
                                                
                     #asta aca parte 5.py
























