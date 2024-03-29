# <a href="https://tyradex.tech/"><img src="https://tyradex.tech/assets/logo.png" alt="Logo Pokémon"/></a> Tyradex for Python

<div align="center">

[![LassaInora - Tyradex](https://img.shields.io/static/v1?label=LassaInora&message=Tyradex&color=yellow&logo=github)](https://github.com/LassaInora/Tyradex "Go to GitHub repo")
[![GitHub tag](https://img.shields.io/github/tag/LassaInora/Tyradex?include_prereleases=&sort=semver&color=orange)](https://github.com/LassaInora/Tyradex/releases/)
[![stars - Tyradex](https://img.shields.io/github/stars/LassaInora/Tyradex?style=social)](https://github.com/LassaInora/Tyradex)
[![forks - Tyradex](https://img.shields.io/github/forks/LassaInora/Tyradex?style=social)](https://github.com/LassaInora/Tyradex)

[![PyPI version](https://badge.fury.io/py/Tyradex.svg)](https://badge.fury.io/py/Tyradex)
[![Supported Versions](https://img.shields.io/pypi/pyversions/Tyradex.svg)](https://pypi.org/project/Tyradex)

___

[![Click for README - French](https://img.shields.io/badge/Click_for_README-Français-red)](README_FRENCH.md)

</div>

<h1 id="1-overview">Overview</h1>
This Python script interacts with the [Tyradex API](https://tyradex.tech/) to retrieve detailed information about Pokémon and Pokémon types. It is designed to provide easy access to details such as Pokédex ID, generation, category, statistics, etc., for individual Pokémon or types. The script is organized into classes representing different aspects of Pokémon data and includes functions to obtain lists of all Pokémon and types.

<h1 id="2-summary">Summary</h1>
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

<h1 id="3-how_to_use">How to use</h1>

<h2 id="3_1-installation">Installation</h2>

<h2 id="3_2-librairy">Librairy</h2>

<h3 id="3_2_1-pokemon">Pokemon</h3>

<h4 id="3_2_1_1-exemple">Exemple</h4>
```python
import Tyradex

ALL = Tyradex.Pokemon.all()
LAST = ALL[-1].pokedex_id


def poke_team(x):
    x = str(x)
    cut = []
    mem = ''
    for digit in x:
        if int(mem + digit) > LAST:
            cut.append(int(mem))
            mem = ''
        mem += digit
    cut.append(int(mem))

    return [Tyradex.Pokemon.get(obj) for obj in cut][:6]


print(poke_team(306100860922888193))
print(poke_team(306429397701885952))
print(poke_team(336443651628728322))
```
```
>> [<0306:Galeking>, <1008:Miraidon>, <0609:Lugulabre>, <0228:Malosse>, <0881:Galvagla>, <0093:Spectrum>]
>> [<0306:Galeking>, <0429:Magirêve>, <0397:Étourvol>, <0701:Brutalibré>, <0885:Fantyrm>, <0952:Scovilain>]
>> [<0336:Séviper>, <0443:Griknot>, <0651:Boguérisse>, <0628:Gueriaigle>, <0728:Otaquin>, <0322:Chamallot>]
```

<h4 id="3_2_1_2-functions">Functions</h4>
  - `Pokemon.all()`
    - Lists all Pokémon.
  - `Pokemon.get(<identifiant>, <<region>>)`
    - Give the identified Pokémon.
    - `<identifiant>`: The name (French or English) or the national pokédex number of the pokémon
    - `<<region>>`: (optional) The Pokémon region

<h4 id="3_2_1_3-properties">Properties</h4>
  - `pokemon.pokedex_id`
    - The number in the national pokédex
  - `pokemon.generation`
    - The publication generation
  - `pokemon.category`
    - The Pokémon category
  - `pokemon.name`
    - The name of the Pokémon
  - `pokemon.sprites`
    - The sprites of the Pokémon
  - `pokemon.types`
    - The types of the Pokémon
  - `pokemon.talents`
    - The list of Pokémon talents
  - `pokemon.stats`
    - The stats of the Pokémon
  - `pokemon.resistances`
    - Pokémon resistances
  - `pokemon.evolution`
    - Pokémon evolutions
  - `pokemon.height`
    - The size of the Pokémon
  - `pokemon.weight`
    - The weight of the Pokémon
  - `pokemon.egg_groups`
    - The list of Pokémon egg's group
  - `pokemon.sexe`
    - The percentage chance of gender appearing
  - `pokemon.catch_rate`
    - Pokémon capture rate
  - `pokemon.level_100`
    - The number of experience of the Pokémon to reach level 100
  - `pokemon.formes`
    - Alternative forms of the Pokémon

<h3 id="3_2_2-generation">Generation</h3>

<h4 id="3_2_2_1-exemple">Exemple</h4>

<h4 id="3_2_2_2-functions">Functions</h4>

<h4 id="3_2_2_3-properties">Properties</h4>

<h3 id="3_2_3-type">Type</h3>

<h4 id="3_2_3_1-exemple">Exemple</h4>

<h4 id="3_2_3_2-functions">Functions</h4>

<h4 id="3_2_3_3-properties">Properties</h4>

<h2 id="3_3-command_line">Command line</h2>

<h1 id="4-dependencies">Dependencies</h1>

<h1 id="5-api_reference">API Reference</h1>

<h1 id="6-contributors">Contributors</h1>

<h2 id="6_1-api">API</h2>

<h2 id="6_2-python_adaptation">Python Adaptation</h2>

<h1 id="7-license">Licence</h1>