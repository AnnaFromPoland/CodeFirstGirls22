import requests

pokemons_IDs = [1, 4, 9, 10, 17, 19]
pokemons = {}

api_url_base = "https://pokeapi.co/api/v2/"

for ID in pokemons_IDs:
    api_url = api_url_base + "pokemon/" + str(ID) + "/"
    response = requests.get(api_url)
    abilities = []
    for ability in response.json()["abilities"]:
        abilities.append(ability["ability"]["name"])
    pokemons[response.json()["name"]] = abilities

with open('./pokemons.txt', 'w') as pokemons_file:
    pokemons_file.write("{\n")
    for key in pokemons.keys():
        pokemons_file.write("'{}':'{}'\n".format(key, pokemons[key]))
    pokemons_file.write("}")
