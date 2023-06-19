"""
Utils for the project "Tratamiento de datos en APIs"
"""
import os
import json 

"""
Save JSON data 
@Params: json_data: json data 
@Params: title:     name of the output file    
"""

def save_json_data(json_data, title):
    
    # Creamos la carpeta "output_files" (si no existen aun)
    if not os.path.exists('output_files'):
        os.makedirs('output_files')

    # Path
    json_path = f'output_files/{title}.json'

    # Guardar datos JSON 
    with open(json_path, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f'JSON guardado en: "{json_path}".')
