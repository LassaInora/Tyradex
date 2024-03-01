# <a href="https://tyradex.tech/"><img src="https://tyradex.tech/assets/logo.png" alt="Logo Pokémon"/></a> Tyradex for Python

<div align="center">

[![LassaInora - Tyradex](https://img.shields.io/static/v1?label=LassaInora&message=Tyradex&color=yellow&logo=github)](https://github.com/LassaInora/Tyradex "Go to GitHub repo")
[![GitHub tag](https://img.shields.io/github/tag/LassaInora/Tyradex?include_prereleases=&sort=semver&color=orange)](https://github.com/LassaInora/Tyradex/releases/)
[![stars - Tyradex](https://img.shields.io/github/stars/LassaInora/Tyradex?style=social)](https://github.com/LassaInora/Tyradex)
[![forks - Tyradex](https://img.shields.io/github/forks/LassaInora/Tyradex?style=social)](https://github.com/LassaInora/Tyradex)

[![PyPI version](https://badge.fury.io/py/Tyradex.svg)](https://badge.fury.io/py/Tyradex)
[![Supported Versions](https://img.shields.io/pypi/pyversions/Tyradex.svg)](https://pypi.org/project/Tyradex)

___

[![Click for README - English](https://img.shields.io/badge/Click_for_README-English-red)](README.md)

</div>

<h1 id="1-overview">Aperçu</h1>

Ce script python interagi avec l'[API Tyradex](https://tyradex.tech/).

Cette librairie se veut simple d'usage pour récupérer les informations d'un pokémon, d'un type ou d'une génération.

<h1 id="2-summary">Sommaire</h1>
<details markdown="1">
  <summary>Table of Contents</summary>

-   [1 Overview](#1-overview)
-   [2 Summary](#2-summary)
-   [3 How to use](#3-how_to_use)
    *   [3.1 Installation](#3_1-installation)
    *   [3.2 Librairy](#3_2-librairy)
        +   [3.2.1 Pokemon](#3_2_1-pokemon)
            *   [3.2.1.1 Exemple](#3_2_1_1-exemple)
            *   [3.2.1.2 Functions](#3_2_1_2-functions)
            *   [3.2.1.3 Properties](#3_2_1_3-properties)
        +   [3.2.2 Generation](#3_2_2-generation)
            *   [3.2.2.1 Exemple](#3_2_2_1-exemple)
            *   [3.2.2.2 Functions](#3_2_2_2-functions)
            *   [3.2.2.3 Properties](#3_2_2_3-properties)
        +   [3.2.3 Type](#3_2_3-type)
            *   [3.2.3.1 Exemple](#3_2_3_1-exemple)
            *   [3.2.3.2 Functions](#3_2_3_2-functions)
            *   [3.2.3.3 Properties](#3_2_3_3-properties)
    *   [3.3 Command line](#3_3-command_line)
-   [4 Dependencies](#4-dependencies)
-   [5 API Reference](#5-api_reference)
-   [6 Contributors](#6-contributors)
    *   [6.1 API](#6_1-api)
    *   [6.2 Python Adaptation](#6_2-python_adaptation)
-   [7 Licence](#7-license)

</details>

<h1 id="3-how_to_use">Comment l'utiliser</h1>

<h2 id="3_1-installation">Installation</h2>

Vous pouvez installer cette librairie grâce à [Pypi](https://pypi.org/project/Tyradex/) via la commande

`python -m pip install Tyradex`

<h2 id="3_2-librairy">Librairie</h2>

<h3 id="3_2_1-pokemon">Pokemon</h3>

<h4 id="3_2_1_1-exemple">Exemple</h4>

```python
import Tyradex

TOUS = Tyradex.Pokemon.all()
DERNIER = TOUS[-1].pokedex_id


def equipe_poke(x):
    x = str(x)
    coupe = []
    mem = ''
    for digit in x:
        if int(mem + digit) > DERNIER:
            coupe.append(int(mem))
            mem = ''
        mem += digit
    coupe.append(int(mem))

    return [Tyradex.Pokemon.get(obj) for obj in coupe][:6]


print(equipe_poke(306100860922888193))
print(equipe_poke(306429397701885952))
print(equipe_poke(336443651628728322))
```
```
>> [<0306:Galeking>, <1008:Miraidon>, <0609:Lugulabre>, <0228:Malosse>, <0881:Galvagla>, <0093:Spectrum>]
>> [<0306:Galeking>, <0429:Magirêve>, <0397:Étourvol>, <0701:Brutalibré>, <0885:Fantyrm>, <0952:Scovilain>]
>> [<0336:Séviper>, <0443:Griknot>, <0651:Boguérisse>, <0628:Gueriaigle>, <0728:Otaquin>, <0322:Chamallot>]
```

<h4 id="3_2_1_2-functions">Fonctions</h4>
  - `Pokemon.all()`
    - Liste de tous les Pokémons.
  - `Pokemon.get(<identifiant>, <<région>>)`
    - Donne le Pokémon identifié.
    - `<identifiant>`: Le nom (Français ou Anglais) ou le numéro de Pokédex national du Pokémon.
    - `<<région>>`: (optionnel) La région du Pokémon.

<h4 id="3_2_1_3-properties">Propriétés</h4>
  - `pokemon.pokedex_id`
    - Le numéro dans le pokédex national.
  - `pokemon.generation`
    - La génération d'apparition.
  - `pokemon.category`
    - La catégorie du Pokémon
  - `pokemon.name`
    - Le nom du Pokémon
  - `pokemon.sprites`
    - Les sprites du Pokémon
  - `pokemon.types`
    - Le ou les types du Pokémon
  - `pokemon.talents`
    - La liste des talent du Pokémon
  - `pokemon.stats`
    - Les stats du Pokémon
  - `pokemon.resistances`
    - Les résistances du Pokémon
  - `pokemon.evolution`
    - La famille évolutive du Pokémon
  - `pokemon.height`
    - La taille du Pokémon
  - `pokemon.weight`
    - Le poids du Pokémon
  - `pokemon.egg_groups`
    - La liste de ces groupes d'œufs
  - `pokemon.sexe`
    - Le pourcentage de chance d'apparition du sexe.
  - `pokemon.catch_rate`
    - Le taux de capture
  - `pokemon.level_100`
    - Le nombre d'expériences nécessaire pour atteindre le niveau 100.
  - `pokemon.formes`
    - Les formes alternatives du Pokémon

<h3 id="3_2_2-generation">Generation</h3>

<h4 id="3_2_2_1-exemple">Exemple</h4>

<h4 id="3_2_2_2-functions">Functions</h4>

<h4 id="3_2_2_3-properties">Properties</h4>

<h3 id="3_2_3-type">Type</h3>

<h4 id="3_2_3_1-exemple">Exemple</h4>

<h4 id="3_2_3_2-functions">Functions</h4>

<h4 id="3_2_3_3-properties">Properties</h4>

<h2 id="3_3-command_line">Command line</h2>

L'utilisation en ligne de commande reprend strictement l'utilisation de l'API tel qu'elle est décrite dans 
[sa documentation](https://tyradex.vercel.app/docs) en omettant la racine de l'API.

```bash
python -m Tyradex pokemon/242
```

<h1 id="4-dependencies">Dependencies</h1>

- [`requests`](https://pypi.org/project/requests/) : Requests is an HTTP library, written in Python, for human beings.
  + Utile pour les appels à l'API.
  ```bash 
    python -m pip install request
    ```
- [`unidecode`](https://pypi.org/project/Unidecode/) : Transliterate Unicode text into plain 7-bit ASCII.
  + Utile pour uniformiser les textes.
  ```bash
    python -m pip install Unidecode
  ```
- [`pillow`](https://pypi.org/project/pillow/) : Python Imaging Library (Fork)
  + Utile pour la gestion des images.
  ```bash 
    python -m pip install pillow
    ```

<h1 id="5-api_reference">API Reference</h1>

- Le script interagit avec l'[API Tyradex](https://tyradex.vercel.app/) hébergée sur https://tyradex.tech/api/v1/.
- Consultez la [documentation](https://tyradex.vercel.app/docs) de l'API pour plus de détails sur les points d'extrémité disponibles et la structure des données.

<h1 id="6-contributors">Contributors</h1>

<h2 id="6_1-api">API</h2>

- [Yarkis](https://github.com/Yarkis01)
- [Ashzuu](https://github.com/Ashzuu)

<h2 id="6_2-python_adaptation">Python Adaptation</h2>

- [LassaInora](https://github.com/LassaInora)


<h1 id="7-license">Licence</h1>

Ce projet est sous licence [MIT License](https://github.com/Yarkis01/PokeAPI/blob/main/LICENSE).
