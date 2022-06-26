import requests
import json

print('Cargando datos...')

def peticion (url):

    response = requests.get(url)

    if response.status_code == 200:
        
      return json.loads(response.text)
    else:
      return None

URL='http://pokeapi.co/api/v2/pokemon/'


for pokemon in peticion(URL)["results"]:
  print(pokemon)