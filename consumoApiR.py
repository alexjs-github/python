from flask import Flask
import requests
import json

print('Cargando datos...')

app = Flask(__name__)

@app.route('/')

def home():
  return 'HOLA ALEXANDER'

app.route("/about")

def about():
  return 'ABOUT'

def peticion (url):

    response = requests.get(url)

    if response.status_code == 200:
        
      return json.loads(response.text)
    else:
      return None

URL='http://pokeapi.co/api/v2/pokemon/'


for pokemon in peticion(URL)["results"]:
  print(pokemon)

if __name__ == '__main__':
  app.run()