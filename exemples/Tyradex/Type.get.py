from src.Tyradex import Type

types = Type.get(2)
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [2] Dragon : 65 pokémons

types = Type.get("Feu")
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [6] Feu : 79 pokémons

types = Type.get(2, 3)
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [39] Dragon - Eau : 5 pokémons

types = Type.get(2, "Combat")
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [37] Dragon - Combat : 3 pokémons

types = Type.get("Feu", 3)
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [111] Feu - Eau : 1 pokémons

types = Type.get("Feu", "Combat")
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [109] Feu - Combat : 6 pokémons

types = Type.get(110)
print(f"[{types.id}] {types} : {len(types.pokemons)} pokémons")
# >> [110] Feu - Dragon : 2 pokémons