import json
import os
import re

fileDir = os.path.dirname(os.path.realpath('__file__'))
GalarDexFileRelative = "..\\pokemonscraping\\GalarDex.json"
GalarDexFile = os.path.join(fileDir, GalarDexFileRelative)

with open(GalarDexFile, 'r') as data_file:
    json_data = data_file.read()

GalarDex = json.loads(json_data)

def get_types_array(Pokedex):
    types =[]
    for pokemon in Pokedex:
        for alternateForm in pokemon['types']:
                types+=(pokemon['types'][alternateForm])
    return sorted(list(set(types)), key=str.lower)

allPokeTypes = get_types_array(GalarDex)

def check_pokemon_types(pokemon, pokeType):
    allPokeTypes = []
    for alternateForm in pokemon['types']:
        allPokeTypes += (pokemon['types'][alternateForm])
    allPokeTypes = sorted(list(set(allPokeTypes)), key=str.lower)
    if pokeType in allPokeTypes:
        return pokemon['name']

def build_types_json(types_array, Pokedex):
    typesJson = {}
    for pokeType in types_array:
        type_json = {}
        type_json['type'] = pokeType
        type_json['pokemon'] = []
        for pokemon in Pokedex:
            checked_pokemon = check_pokemon_types(pokemon, pokeType)
            if checked_pokemon is not None:
                type_json['pokemon'].append(checked_pokemon)
        typesJson[pokeType] = type_json
    return typesJson

galar_types_json = build_types_json(allPokeTypes, GalarDex)

def write_types_file():
    locationsFile = open('GalarTypes.json', 'w')
    locationsFile.write(json.dumps(galar_types_json, indent=4))
    locationsFile.close()

write_types_file()
    
    


