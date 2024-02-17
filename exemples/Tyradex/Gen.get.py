from src.Tyradex import Generation

gen = Generation.get(6)
print(f"{gen} ({gen.from_} → {gen.to}) : {len(gen.pokemons)} pokémons")
# >> Génération 6 (650 → 721) : 72 pokémons
