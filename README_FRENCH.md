# <a href="https://tyradex.tech/"><img src="https://tyradex.tech/assets/logo.png" alt="Logo Pokémon"/></a> Tyradex pour Python
[![PyPI version](https://badge.fury.io/py/Tyradex.svg)](https://badge.fury.io/py/Tyradex)
[![Supported Versions](https://img.shields.io/pypi/pyversions/Tyradex.svg)](https://pypi.org/project/Tyradex)
[![Downloads](https://static.pepy.tech/badge/Tyradex/month)](https://pepy.tech/project/Tyradex)
[![Contributors](https://img.shields.io/github/contributors/LassaInora/Tyradex.svg)](https://github.com/LassaInora/Tyradex/graphs/contributors)

-> 🇺🇸 : [README.md](https://github.com/LassaInora/Tyradex/blob/main/README.md)

## Aperçu
Ce script Python interagit avec l'[API Tyradex](https://tyradex.vercel.app/) pour récupérer des informations détaillées sur les Pokémon et les types de Pokémon. Il est conçu pour fournir un accès facile à des détails tels que l'ID du Pokédex, la génération, la catégorie, les statistiques, etc., pour des Pokémon individuels ou des types. Le script est organisé en classes représentant différents aspects des données Pokémon et inclut des fonctions pour obtenir des listes de tous les Pokémon et types.

## Fonctionnalités
- ### Classe Pokemon :

  - Récupérez des informations détaillées sur un Pokémon spécifique.
  - Accédez à des propriétés telles que l'ID du Pokédex, la génération, la catégorie, les statistiques, etc.

- ### Classe Type :

  - Obtenez des informations sur un type de Pokémon spécifique.
  - Accédez à des propriétés telles que l'ID du type, les résistances et une liste de Pokémon associés à ce type.

- ### Classe Generations :

  - Accédez aux données Pokémon regroupées par différentes générations.

- ### Classes de support :

  - Diverses classes de support pour gérer les noms, les talents, les sprites, les statistiques, les résistances, les évolutions, le sexe et les formes.

- ### Fonctions :

  - `get_all_pokemons` : Récupérez une liste de tous les Pokémon.
  - `get_all_types` : Récupérez une liste de tous les types de Pokémon.

## Comment utiliser
1) ### Installation :

  - Assurez-vous d'avoir Python installé sur votre système.
  - Installez les dépendances requises en utilisant pip install -r requirements.txt.

2) ### Utilisation :

  - Importez le script dans votre projet Python ou exécutez-le en tant que script autonome.
  - Instanciez les classes pertinentes pour interagir avec les Pokémon ou les types.
  - Explorez les fonctions fournies pour obtenir des listes de Pokémon et de types.

```python
# Exemple d'utilisation
from Tyradex import Pokemon, Type, Generations, get_all_pokemons, get_all_types

# Récupérez des informations sur un Pokémon spécifique
dracaufeu = Pokemon('dracaufeu')
print(dracaufeu.name)

# Récupérez des informations sur un type de Pokémon spécifique
type_feu = Type('feu')
print(type_feu.name)

# Récupérez l'ensemble des pokémons d'une génération
gen_6 = Generations.Gen(6)
print(gen_6[42])

# Récupérez une liste de tous les Pokémon et types
tous_les_pokemons = get_all_pokemons()
tous_les_types = get_all_types()
```
## Dépendances
- `requests` : Requests is an HTTP library, written in Python, for human beings.
- `unidecode` : Transliterate Unicode text into plain 7-bit ASCII.

## Référence API
- Le script interagit avec l'API Pokémon hébergée sur https://tyradex.tech/api/v1/.
- Consultez la [documentation de l'API](https://tyradex.tech/docs) pour plus de détails sur les points d'extrémité disponibles et la structure des données.

## Contributeurs
- API créée par:
  - [Yarkis](https://github.com/Yarkis01)
  - [Ashzuu](https://github.com/Ashzuu)
- Adaptation pour python par:
  - [LassaInora](https://github.com/LassaInora)

## Licence
Ce projet est sous licence [MIT License](https://github.com/Yarkis01/PokeAPI/blob/main/LICENSE).
