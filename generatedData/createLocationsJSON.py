import json
import os
import re

fileDir = os.path.dirname(os.path.realpath('__file__'))
GalarDexFileRelative = "..\\pokemonscraping\\GalarDex.json"
GalarDexFile = os.path.join(fileDir, GalarDexFileRelative)

with open(GalarDexFile, 'r') as data_file:
    json_data = data_file.read()

GalarDex = json.loads(json_data)

def get_locations_array(Pokedex):
    locations = []
    for pokemon in Pokedex:
        locations += pokemon['locations_sword']
        locations += pokemon['locations_shield']
    return list(set(locations))

unique_locations = get_locations_array(GalarDex)

def clean_locations(raw_locations):
    Uncatcheable = re.compile(r"([Ee](volve|vent|xpansion)|[Tt]rade|[Gg]ift|[Rr]evive)")
    clean_locations =[location for location in raw_locations if not re.search(Uncatcheable, location)]
    return sorted(clean_locations, key=str.lower)

all_locations = clean_locations(unique_locations)
print(all_locations)
#Sword code is sw Shield code is sw
#returns a pokemon name if it can be found at a given location

def check_pokemon_at(pokemon, location, swsh = "sw"):
    if swsh == "sw":
        if location in pokemon['locations_sword']:
            return pokemon['name']
    if swsh == "sh":
        if location in pokemon['locations_shield']:
            return pokemon['name']

def build_locations_json(locations_array, Pokedex):
    locationsJson = {}
    for location in locations_array:
        location_json = {}
        location_json['location'] = location
        location_json['sword_pokemon'] = []
        location_json['shield_pokemon'] = []
        for pokemon in Pokedex:
            sword_pokemon = check_pokemon_at(pokemon, location, "sw")
            shield_pokemon = check_pokemon_at(pokemon, location, "sh")
            if sword_pokemon is not None:
                location_json['sword_pokemon'].append(sword_pokemon)
            if shield_pokemon is not None:
                location_json['shield_pokemon'].append(shield_pokemon)
        locationsJson[location] = location_json
    return locationsJson

locations_json = build_locations_json(all_locations, GalarDex)

def write_locations_file():
    locationsFile = open('GalarLocations.json', 'w')
    locationsFile.write(json.dumps(locations_json, indent=4))
    locationsFile.close()

write_locations_file()
