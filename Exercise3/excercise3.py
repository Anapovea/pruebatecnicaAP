"""
Ejercicio 3: Tratamiento de datos en APIs

En este enlace encontrarás la documentación de la API de una tienda de mascotas:
https://petstore.swagger.io/
     
    1. 
    Crea tu usuario mediante petición HTTP y posteriormente recupera sus 
    datos llamando al servicio correspondiente.

    2. 
    Recoge mediante petición HTTP, el JSON que retorna el endpoint /pet/findByStatus y
    lista mediante una función los nombres de las mascotas que se hayan vendido.         
    El formato de salida deberá estar formado por la tupla {id, name}.         
    Puedes utilizar la estructura de datos que prefieras.
 
    3. 
    Crea una clase cuyo constructor requiera de la estructura de datos anterior y 
    realiza un método que pueda recorrerla para poder identificar cuantas mascotas 
    se llaman igual.
    Ejemplo de salida: {“William”: 11, “ Floyd”: 2} 

Como output, te pediremos el código (puedes separarlo en archivos como quieras) 
y los resultados de salida de los puntos anteriores.
Recuerda que puedes utilizar el lenguaje que prefieras y cualquier mejora adicional 
será bien considerada
"""


import requests
import json
from utils import save_json_data


"""
EJERCICIO 1
    Crea tu usuario mediante petición HTTP y posteriormente 
    recupera sus datos llamando al servicio correspondiente.
"""

def create_and_get_user():
    
    # URL 
    url_base = 'https://petstore.swagger.io/v2'

    # Endpoint 
    creation_user_endpoint = f'{url_base}/user'

    # Headers 
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Payload para crear el usuario
    user_payload = {
        "id": 333,
        "username": "userName1",
        "firstName": "firstName1",
        "lastName": "lastName1",
        "email": "email@gmail.com",
        "password": "pass099999",
        "phone": "999666333",
        "userStatus": 1
    }

    # Peticion POST (para crear user)
    response = requests.post(creation_user_endpoint, headers=headers, json=user_payload)

    # Verificamos si la peticion es OK (200)
    if response.status_code == 200:
        print('Usuario creado.')
    else:
        print('ERROR creando un usuario (POST).')

    # Endpoint 
    get_user_endpoint = f'{url_base}/user/{user_payload["username"]}'

    # Peticion GET (para obtener los datos de un usuario ya creado)
    response = requests.get(get_user_endpoint, headers=headers)

    # Verificamos si la peticion es OK (200)
    if response.status_code == 200:
        user_data = response.json()
        print('USER DATA:')
        print(json.dumps(user_data, indent=4))
    else:
        print('ERROR al obtener (GET) los datos del usuario.')

    return user_payload


"""
EJERCICIO 2
    Recoge mediante petición HTTP, el JSON que retorna el endpoint /pet/findByStatus y
    lista mediante una función los nombres de las mascotas que se hayan vendido.         
    El formato de salida deberá estar formado por la tupla {id, name}.         
    Puedes utilizar la estructura de datos que prefieras.
"""

def list_sold_pets():
    
    # URL  
    url_base = 'https://petstore.swagger.io/v2'
    
    #Status (sold, available, pending)
    status = 'sold'
    
    # Endpoint 
    find_pets_endpoint = f'{url_base}/pet/findByStatus?status={status}'

    # GET all the pets 
    response = requests.get(find_pets_endpoint)

    # Verificamos si la peticion es OK (200)
    if response.status_code == 200:
            pet_data = response.json() #convertimos el json a objeto en python

            # Declaro una lista vacia  
            pet_names = []
    
            # Obtenemos la tupla ID+name 
            for pet in pet_data:                
                pet_id = pet['id']
                pet_name = pet['name']
                pet_names.append((pet_id, pet_name))
            
            tuple_return = tuple(pet_names)
            print("\n" , tuple_return) #for debugging
            return tuple_return
    else:
        print('Error al obtener (GET) datos.')
        return ()


"""
EJERCICIO 3
     Crea una clase cuyo constructor requiera de la estructura de datos anterior y 
     realiza un método que pueda recorrerla para poder identificar cuantas mascotas se llaman igual.
     Ejemplo de salida: {“William”: 11, “ Floyd”: 2} 
"""

class PetNameCounter:
    
    def __init__(self, pet_names): #constructor
        self.pet_names = pet_names

    def count_same_names(self):
        
        name_counts = {}
        
        for name in self.pet_names:
            if name in name_counts:
                name_counts[name] += 1
            else:
                name_counts[name] = 1
        print("\n" , name_counts)  #for debugging
        return name_counts

"""
    Main con los tres ejercicios
        Ejercicio 1
        Ejercicio 2
        Ejercicio 3
"""

def main():
    
    # EJERCICIO 1
    user_payload = create_and_get_user()
    save_json_data(user_payload, 'user_creation')

    # EJERCICIO 2
    sold_pet_name = list_sold_pets()
    save_json_data(sold_pet_name, 'sold_pet_name')

    # EJERCICIO 3 
    pet_counter = PetNameCounter([name for _, name in sold_pet_name])
    name_counts = pet_counter.count_same_names()
    save_json_data(name_counts, 'repeated_names')   

if __name__ == "__main__":
    main()




