import requests
import urllib.parse

url = "https://graphhopper.com/api/1/route?"
clave = "3db4cfa8-0b90-4bf7-bd17-d3dfb74d97a0"      

def geocodificacion(ubicacion, clave):
    while ubicacion == "":
        ubicacion = input("Ingrese la ubicación nuevamente: ")
        
    url_geocodificacion = "https://graphhopper.com/api/1/geocode?" 
    url = url_geocodificacion + urllib.parse.urlencode({"q":ubicacion, "limit": "1", "key":clave})

    respuesta = requests.get(url)
    datos_json = respuesta.json()
    estado_json = respuesta.status_code                               
    
    if estado_json == 200 and len(datos_json["hits"]) != 0:
        datos_json = requests.get(url).json()

        datos_json = requests.get(url).json()
        latitud=(datos_json["hits"][0]["point"]["lat"])
        longitud=(datos_json["hits"][0]["point"]["lng"])
        nombre = datos_json["hits"][0]["name"]
        valor = datos_json["hits"][0]["osm_value"]
        
        if "country" in datos_json["hits"][0]:
            pais = datos_json["hits"][0]["country"]
        else:
            pais=""
        
        if "state" in datos_json["hits"][0]:
            estado = datos_json["hits"][0]["state"]
        else:
            estado=""
        
        if len(estado) !=0 and len(pais) !=0:
            nueva_ubicacion = nombre + ", " + estado + ", " + pais
        elif len(estado) !=0:
            nueva_ubicacion = nombre + ", " + pais
        else:
            nueva_ubicacion = nombre
        
        print("URL de la API de Geocodificación para " + nueva_ubicacion + " (Tipo de ubicación: " + valor + ")\n" + url)
    else:
        latitud="null"
        longitud="null"
        nueva_ubicacion=ubicacion
        if estado_json != 200:                                  
            print("Estado de la API de Geocodificación: " + str(estado_json) + "\nMensaje de error: " + datos_json["message"])   
    return estado_json,latitud,longitud,nueva_ubicacion

while True:                                                 
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Perfiles de vehículos disponibles en Graphhopper:")          
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("auto, bicicleta, pie, patineta, transporte publico, triciclo")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    perfil=["auto", "bicicleta", "pie", "patineta", "transporte publico", "triciclo"]                              
    vehiculo = input("Ingrese un perfil de vehículo de la lista anterior: ")
    if vehiculo.lower() in ["salir", "s"]:
        break
    elif vehiculo in perfil:
        vehiculo = vehiculo
    else: 
        vehiculo = "auto"
        print("No se ingresó un perfil de vehículo válido. Se utilizará el perfil de auto.")
    loc1 = input("Ciudad de Inicio: ")
    if loc1.lower() in ["salir", "s"]:                 
        break
    orig = geocodificacion(loc1, clave)
    print(orig)

    loc2 = input("Ciudad de Término: ")
    if loc2.lower() in ["salir", "s"]:                
        break
    dest = geocodificacion(loc2, clave)
    print("=================================================")                                
    if orig[0] == 200 and dest[0] == 200:                      
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])
        urls = url + urllib.parse.urlencode({"key":clave, "vehicle":vehiculo}) + op + dp    
        estado_rutas = requests.get(urls).status_code
        datos_rutas = requests.get(urls).json()
        print("Estado de la API de Enrutamiento: " + str(estado_rutas) + "\nURL de la API de Enrutamiento:\n" + urls)  
        print("=================================================")
        print("Direcciones desde " + orig[3] + " hasta " + dest[3] + " en " + vehiculo)         
        print("=================================================")
        if estado_rutas == 200:
            millas = round((datos_rutas["paths"][0]["distance"])/1000/1.61, 2)                        
            km = round((datos_rutas["paths"][0]["distance"])/1000, 2)                               
            tiempo = datos_rutas["paths"][0]["time"]/1000
            horas = int(tiempo // 3600)
            minutos = int((tiempo % 3600) // 60)
            segundos = int(tiempo % 60)
            print("Distancia Recorrida: {0:.2f} millas / {1:.2f} km".format(millas, km))      
            print("Duración del Viaje: {0:02d}:{1:02d}:{2:02d}".format(horas, minutos, segundos))          
            print("=================================================")                           
            for cada in range(len(datos_rutas["paths"][0]["instructions"])):
                ruta = datos_rutas["paths"][0]["instructions"][cada]["text"]                                   
                distancia = round(datos_rutas["paths"][0]["instructions"][cada]["distance"]/1000, 2)
                print("{0} ( {1:.2f} km / {2:.2f} millas )".format(ruta, distancia, distancia/1.61))
            print("=============================================")                                    
        else:                                                                      
            print("Mensaje de error: " + datos_rutas["message"])
            print("*************************************************")
























