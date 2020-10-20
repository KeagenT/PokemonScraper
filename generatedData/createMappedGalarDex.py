import json
import os
import re

fileDir = os.path.dirname(os.path.realpath('__file__'))
GalarDexFileRelative = "..\\pokemonscraping\\GalarDex.json"
GalarDexFile = os.path.join(fileDir, GalarDexFileRelative)

with open(GalarDexFile, 'r') as data_file:
    json_data = data_file.read()

GalarDex = json.loads(json_data)

def build_mapped_dex_json(Pokedex):
    mappedDex = {}
    for pokemon in Pokedex:
        pokemonName = pokemon['name']
        mappedDex[pokemonName] = pokemon
    return mappedDex

mapped_galar_dex = build_mapped_dex_json(GalarDex)

def write_mapped_dex_file():
    dexFile = open('MappedGalarDex.json', 'w')
    dexFile.write(json.dumps(mapped_galar_dex, indent=4))
    dexFile.close()

write_mapped_dex_file()