from src.Tyradex import Pokemon

nb_bonbon = lambda xp: xp // 30000 + (1 if xp % 30000 != 0 else 0)

pokemon = Pokemon.get(778)
print(f"[{pokemon.pokedex_id:04}] {pokemon} : {nb_bonbon(pokemon.level_100)} Bonbon Exp. Xl")
# >> [0778] Mimiqui : 34 Bonbon Exp. Xl

pokemon = Pokemon.get("Yveltal")
print(f"[{pokemon.pokedex_id:04}] {pokemon} : {nb_bonbon(pokemon.level_100)} Bonbon Exp. Xl")
# >> [0717] Yveltal : 42 Bonbon Exp. Xl
