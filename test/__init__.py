import time

from src.Tyradex import *


def testing(pok: Pokemon, maker=...):
    if maker is ...:
        maker = lambda *args, **kwargs: ''
    try:
        maker("pok:", pok)
        maker("pokedex_id:", pok.pokedex_id)
        maker("generation:", pok.generation)
        maker("category:", pok.category)
        maker("name:", pok.name)
        maker("\t", "fr:", pok.name.fr)
        maker("\t", "en:", pok.name.en)
        maker("\t", "jp:", pok.name.jp)
        maker("sprites:", pok.sprites)
        maker("\t", "regular:", pok.sprites.regular)
        maker("\t", "shiny:", pok.sprites.shiny)
        maker("\t", "gmax:", pok.sprites.gmax)
        maker("\t\t", "regular:", pok.sprites.gmax.regular)
        maker("\t\t", "shiny:", pok.sprites.gmax.shiny)
        maker("types:", pok.types)
        maker("\t", "id:", pok.types.id)
        maker("\t", "name:", pok.types.name)
        maker("\t\t", "fr:", pok.types.name.fr)
        maker("\t\t", "en:", pok.types.name.en)
        maker("\t\t", "jp:", pok.types.name.jp)
        maker("\t", "sprites:", pok.types.sprites)
        maker("\t", "resistances:", pok.types.resistances)
        maker("\t", "pokemons:", pok.types.pokemons)
        maker("talents:", pok.talents)
        if len(pok.talents) > 0:
            maker("\t", "]:", pok.talents[0])
            maker("\t\t", "name:", pok.talents[0].name)
            maker("\t\t", "talent_cache:", pok.talents[0].talent_cache)
        maker("stats:", pok.stats)
        maker("\t", "hp_:", pok.stats.hp_)
        maker("\t", "atk_:", pok.stats.atk_)
        maker("\t", "def_:", pok.stats.def_)
        maker("\t", "spe_atk_:", pok.stats.spe_atk_)
        maker("\t", "spe_def_:", pok.stats.spe_def_)
        maker("\t", "vit_:", pok.stats.vit_)
        maker("resistances:", pok.resistances)
        if len(pok.resistances) > 0:
            maker("\t", "]:", pok.resistances[0])
            maker("\t\t", "name:", pok.resistances[0].name)
            maker("\t\t", "multiplier:", pok.resistances[0].multiplier)
        maker("evolution:", pok.evolution)
        maker("\t", "pre:", pok.evolution.pre)
        if len(pok.evolution.pre) > 0:
            maker("\t\t", "]:", pok.evolution.pre[0])
            maker("\t\t\t", "pokedex_id:", pok.evolution.pre[0].pokedex_id)
            maker("\t\t\t", "name:", pok.evolution.pre[0].name)
            maker("\t\t\t", "condition:", pok.evolution.pre[0].condition)
        maker("\t", "next:", pok.evolution.next)
        if len(pok.evolution.next) > 0:
            maker("\t\t", "]:", pok.evolution.next[0])
            maker("\t\t\t", "pokedex_id:", pok.evolution.next[0].pokedex_id)
            maker("\t\t\t", "name:", pok.evolution.next[0].name)
            maker("\t\t\t", "condition:", pok.evolution.next[0].condition)
        maker("\t", "mega:", pok.evolution.mega)
        if len(pok.evolution.mega) > 0:
            maker("\t\t", "]:", pok.evolution.mega[0])
            maker("\t\t\t", "orbe:", pok.evolution.mega[0].orbe)
            maker("\t\t\t", "sprites:", pok.evolution.mega[0].sprites)
            maker("\t\t\t\t", "regular:", pok.evolution.mega[0].sprites.regular)
            maker("\t\t\t\t", "shiny:", pok.evolution.mega[0].sprites.shiny)
        maker("height:", pok.height)
        maker("weight:", pok.weight)
        maker("egg_groups:", pok.egg_groups)
        if len(pok.egg_groups) > 0:
            maker("\t", "]:", pok.egg_groups[0])
        maker("sexe:", pok.sexe)
        maker("\t", "male:", pok.sexe.male)
        maker("\t", "female:", pok.sexe.female)
        maker("catch_rate:", pok.catch_rate)
        maker("level_100:", pok.level_100)
        maker("forme:", pok.forme)
        if len(pok.forme) > 0:
            maker("\t", "]:", pok.forme[0])
            maker("\t\t", "region:", pok.forme[0].region)
            maker("\t\t", "name:", pok.forme[0].name)
    except Exception as e:
        time.sleep(0.3)
        print(f"\rPOKEMON : [{pok.pokedex_id}] {pok.name} : {e}")
        raise e


if __name__ == '__main__':
    # error = {'count': 0, 'errors': []}
    # print(f"\r[{' ' * 100}] {0:3}% : ({0:04}/1017)", end='')
    # for pok_id in range(0, 1018):
    #     prct = round(pok_id * 100 / 1017)
    #     try:
    #         testing(Pokemon(pok_id))
    #     except Exception as e:
    #         error['count'] += 1
    #         error['errors'].append(e)
    #     print(f"\r[{'#' * prct}{' ' * (100 - prct)}] {prct:3}% : ({pok_id:04}/1017)", end='')
    # print(f'\r{error["count"]} erreurs.')
    # for err in set(error['errors']):
    #     print(f"- {err}")

    testing(Pokemon(778), print)