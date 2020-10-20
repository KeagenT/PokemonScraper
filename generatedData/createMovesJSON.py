import json
import os
import re

fileDir = os.path.dirname(os.path.realpath('__file__'))
GalarDexFileRelative = "..\\pokemonscraping\\GalarDex.json"
GalarDexFile = os.path.join(fileDir, GalarDexFileRelative)

with open(GalarDexFile, 'r') as data_file:
    json_data = data_file.read()

GalarDex = json.loads(json_data)

def get_moves_array(Pokedex):
    moves = []
    for pokemon in Pokedex:
        moves += pokemon['moves']
    return sorted(list(set(moves)), key=str.lower)

all_moves = get_moves_array(GalarDex)

def check_pokemon_moves(pokemon, move):
    if move in pokemon['moves']:
        return pokemon['name']

def build_moves_json(moves_array, Pokedex):
    movesJson = {}
    for move in moves_array:
        move_json = {}
        move_json['move'] = move
        move_json['pokemon'] = []
        for pokemon in Pokedex:
            checked_pokemon = check_pokemon_moves(pokemon, move)
            if checked_pokemon is not None:
                move_json['pokemon'].append(checked_pokemon)
        movesJson[move] = move_json
    return movesJson

moves_json = build_moves_json(all_moves, GalarDex)

def write_moves_file():
    movesFile = open('GalarMoves.json', 'w')
    movesFile.write(json.dumps(moves_json, indent=4))
    movesFile.close()

write_moves_file()


