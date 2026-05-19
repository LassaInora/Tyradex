class _tyradex_object:
    def __init__(self, data):
        self._data = data

class Pokemon(_tyradex_object):
    def __init__(self, data):
        super().__init__(data)

    @property
    def pokedex_id(self):
        """ The pokedex id of the pokemon.
        
        Returns:
            int: The pokedex id of the pokemon.
        """
        return self._data.get("pokedex_id")

    @property
    def generation(self):
        """ The generation of the pokemon.
        
        Returns:
            int: The generation of the pokemon.
        """
        return self._data.get("generation")

    @property
    def category(self):
        """ The category of the pokemon.
        
        Returns:
            str: The category of the pokemon.
        """
        return self._data.get("pokedex_id")

    @property
    def name(self):
        """ The name of the pokemon.
        
        Returns:
            Name: The name of the pokemon.
        """
        class Name(_tyradex_object):
            @property
            def fr(self):
                """ The french name of the pokemon.
                
                Returns:
                    str: The french name of the pokemon.
                """
                return self._data.get("fr")
            
            @property
            def en(self):
                """ The english name of the pokemon.
                
                Returns:
                    str: The english name of the pokemon.
                """
                return self._data.get("en")
            
            @property
            def jp(self):
                """ The japanese name of the pokemon.
                
                Returns:
                    str: The japanese name of the pokemon.
                """
                return self._data.get("jp")

        return Name(self._data.get("name"))

    @property
    def sprites(self):
        """ The sprites of the pokemon.
        
        Returns:
            Sprites: The sprites of the pokemon.
        """
        class Sprites(_tyradex_object):
            @property
            def regular(self):
                """ The regular sprite of the pokemon.
                
                Returns:
                    str: The regular sprite of the pokemon.
                """
                return self._data.get("regular")
            
            @property
            def shiny(self):
                """ The shiny sprite of the pokemon.
                
                Returns:
                    str: The shiny sprite of the pokemon.
                """
                return self._data.get("shiny")
            
            @property
            def gmax(self):
                """ The gmax sprite of the pokemon.
                
                Returns:
                    str: The gmax sprite of the pokemon.
                """
                return self._data.get("gmax")

        return Sprites(self._data.get("sprites"))

    @property
    def types(self):
        """ The types of the pokemon.
        
        Returns:
            list: The types of the pokemon.
        """
        class Type(_tyradex_object):
            @property
            def name(self):
                """ The name of the type.
                
                Returns:
                    str: The name of the type.
                """
                return self._data.get("name")
            
            @property
            def image(self):
                """ The image of the type.
                
                Returns:
                    str: The image of the type.
                """
                return self._data.get("image")

        return [Type(type_data) for type_data in self._data.get("types", [])]

    @property
    def talents(self):
        """ The talents of the pokemon.
        
        Returns:
            list[Talent]: The talents of the pokemon.
        """
        class Talent(_tyradex_object):
            @property
            def name(self):
                """ The name of the talent.
                
                Returns:
                    str: The name of the talent.
                """
                return self._data.get("name")
            
            @property
            def tc(self):
                """ If the talent is a hidden talent or not.
                
                Returns:
                    bool: The tc of the talent.
                """
                return self._data.get("tc")

        return [Talent(talent_data) for talent_data in self._data.get("talents", [])]

    @property
    def stats(self):
        """ The stats of the pokemon.
        
        Returns:
            Stats: The stats of the pokemon.
        """
        class Stats(_tyradex_object):
            @property
            def hp(self):
                """ The hp stat of the pokemon.
                
                Returns:
                    int: The hp stat of the pokemon.
                """
                return self._data.get("hp")
            
            @property
            def attack(self):
                """ The attack stat of the pokemon.
                
                Returns:
                    int: The attack stat of the pokemon.
                """
                return self._data.get("atk")
            
            @property
            def defense(self):
                """ The defense stat of the pokemon.
                
                Returns:
                    int: The defense stat of the pokemon.
                """
                return self._data.get("def")
            
            @property
            def sp_attack(self):
                """ The special attack stat of the pokemon.
                
                Returns:
                    int: The special attack stat of the pokemon.
                """
                return self._data.get("spe_atk")
            
            @property
            def sp_defense(self):
                """ The special defense stat of the pokemon.
                
                Returns:
                    int: The special defense stat of the pokemon.
                """
                return self._data.get("spe_def")
            
            @property
            def speed(self):
                """ The speed stat of the pokemon.
                
                Returns:
                    int: The speed stat of the pokemon.
                """
                return self._data.get("vit")
        return Stats(self._data.get("stats"))

    @property
    def resistances(self):
        """ The resistances of the pokemon.
        
        Returns:
            list[str]: The resistances of the pokemon.
        """
        class Resistance(_tyradex_object):
            @property
            def name(self):
                """ The name of the resistance.
                
                Returns:
                    str: The name of the resistance.
                """
                return self._data.get("name")
            
            @property
            def multiplier(self):
                """ The multiplier of the resistance.
                
                Returns:
                    float: The multiplier of the resistance.
                """
                return self._data.get("multiplier")
        return [Resistance(resistance_data) for resistance_data in self._data.get("resistances", [])]

    @property
    def evolution(self):
        """ The evolution of the pokemon.
        
        Returns:
            list: The evolution of the pokemon.
        """
        class Evolution(_tyradex_object):
            @property
            def pre(self):
                """ The pre-evolution of the pokemon.

                Returns:
                    str: The pre-evolution of the pokemon.
                """
                class PreEvolution(_tyradex_object):
                    @property
                    def pokedex_id(self):
                        """ The pokedex id of the pre-evolution.

                        Returns:
                            int: The pokedex id of the pre-evolution.
                        """
                        return self._data.get("pokedex_id")
                    
                    @property
                    def name(self):
                        """ The name of the pre-evolution.

                        Returns:
                            str: The name of the pre-evolution.
                        """
                        return self._data.get("name")
                    
                    @property
                    def condition(self):
                        """ The condition to evolve into the pokemon.

                        Returns:
                            str: The condition to evolve into the pokemon.
                        """
                        return self._data.get("condition")
                return [PreEvolution(pre_data) for pre_data in self._data.get("pre", [])]
            
            @property
            def next(self):
                """ The next evolution of the pokemon.

                Returns:
                    str: The next evolution of the pokemon.
                """
                class NextEvolution(_tyradex_object):
                    @property
                    def pokedex_id(self):
                        """ The pokedex id of the next evolution.

                        Returns:
                            int: The pokedex id of the next evolution.
                        """
                        return self._data.get("pokedex_id")
                    
                    @property
                    def name(self):
                        """ The name of the next evolution.

                        Returns:
                            str: The name of the next evolution.
                        """
                        return self._data.get("name")
                    
                    @property
                    def condition(self):
                        """ The condition to evolve into the next evolution.

                        Returns:
                            str: The condition to evolve into the next evolution.
                        """
                        return self._data.get("condition")
                return [NextEvolution(next_data) for next_data in self._data.get("next", [])]

                @property
                def mega(self):
                    """ The mega evolution of the pokemon.

                    Returns:
                        list[MegaEvolution]: The mega evolution of the pokemon.
                    """
                    class MegaEvolution(_tyradex_object):
                        @property
                        def orbe(self):
                            """ The orbe of the mega evolution.

                            Returns:
                                str: The orbe of the mega evolution.
                            """
                            return self._data.get("orbe")
                        
                        @property
                        def sprites(self):
                            """ The sprites of the mega evolution.

                            Returns:
                                str: The sprites of the mega evolution.
                            """
                            class Sprites(_tyradex_object):
                                @property
                                def regular(self):
                                    """ The regular sprite of the mega evolution.
                                    
                                    Returns:
                                        str: The regular sprite of the mega evolution.
                                    """
                                    return self._data.get("regular")
                                
                                @property
                                def shiny(self):
                                    """ The shiny sprite of the mega evolution.
                                    
                                    Returns:
                                        str: The shiny sprite of the mega evolution.
                                    """
                                    return self._data.get("shiny")
                            return Sprites(self._data.get("sprites"))
            
                    return [MegaEvolution(mega_data) for mega_data in self._data.get("mega", [])]
        return Evolution(self._data.get("evolution"))

    @property
    def height(self):
        """ The height of the pokemon.

        Returns:
            Height: The height of the pokemon.
        """
        class Height(float):
            def __str__(self):
                return f"{self} m"
        return Height(self._data.get("height").replace(" m", "").replace(",", "."))

    @property
    def weight(self):
        """ The weight of the pokemon.

        Returns:
            float: The weight of the pokemon.
        """
        class Weight(float):
            def __str__(self):
                return f"{self} kg"
        return Weight(self._data.get("weight").replace(" kg", "").replace(",", "."))

    @property
    def egg_groups(self):
        """ The egg groups of the pokemon.

        Returns:
            list[str]: The egg groups of the pokemon.
        """
        return self._data.get("egg_groups")

    @property
    def sexe(self):
        """ The sexe of the pokemon.

        Returns:
            Sexe: The sexe of the pokemon.
        """
        class Sexe(_tyradex_object):
            @property
            def male(self):
                """ If the pokemon can be male.

                Returns:
                    float: The percentage of the pokemon being male.
                """
                return self._data.get("male")
            
            @property
            def female(self):
                """ If the pokemon can be female.

                Returns:
                    float: The percentage of the pokemon being female.
                """
                return self._data.get("female")
        return Sexe(self._data.get("sexe"))

    @property
    def catch_rate(self):
        """ The catch rate of the pokemon.

        Returns:
            int: The catch rate of the pokemon.
        """
        return self._data.get("catch_rate")

    @property
    def level_100(self):
        """ How many xp the pokemon has at level 100.

        Returns:
            int: The xp required for the pokemon to reach level 100.
        """
        return self._data.get("level_100")

    @property
    def formes(self):
        """ The formes of the pokemon.

        Returns:
            list[Forme]: The formes of the pokemon.
        """
        class Forme(_tyradex_object):
            @property
            def region(self):
                """ The region of the forme.

                Returns:
                    str: The region of the forme.
                """
                return self._data.get("region")
            
            @property
            def name(self):
                """ The name of the forme.

                Returns:
                    str: The name of the forme.
                """
                class Name(_tyradex_object):
                    @property
                    def fr(self):
                        """ The french name of the forme.
                        
                        Returns:
                            str: The french name of the forme.
                        """
                        return self._data.get("fr")
                    
                    @property
                    def en(self):
                        """ The english name of the forme.
                        
                        Returns:
                            str: The english name of the forme.
                        """
                        return self._data.get("en")
                    
                    @property
                    def jp(self):
                        """ The japanese name of the forme.
                        
                        Returns:
                            str: The japanese name of the forme.
                        """
                        return self._data.get("jp")
                return Name(self._data.get("name"))
        return [Forme(forme_data) for forme_data in self._data.get("formes", [])]

class Generation(_tyradex_object):
    @property
    def generation(self):
        """ The generation number.

        Returns:
            int: The generation number.
        """
        return self._data.get("generation")

    @property
    def from_(self):
        """ The first pokedex id of the generation.

        Returns:
            int: The first pokedex id of the generation.
        """
        return self._data.get("from")

    @property
    def to(self):
        """ The last pokedex id of the generation.

        Returns:
            int: The last pokedex id of the generation.
        """
        return self._data.get("to")

class Type(_tyradex_object):
    @property
    def id(self):
        """ The id of the type.

        Returns:
            str: The id of the type.
        """
        return self._data.get("id")

    @property
    def name(self):
        """ The name of the type.

        Returns:
            str: The name of the type.
        """
        class Name(_tyradex_object):
            @property
            def fr(self):
                """ The french name of the type.
                
                Returns:
                    str: The french name of the type.
                """
                return self._data.get("fr")
            
            @property
            def en(self):
                """ The english name of the type.
                
                Returns:
                    str: The english name of the type.
                """
                return self._data.get("en")
            
            @property
            def jp(self):
                """ The japanese name of the type.
                
                Returns:
                    str: The japanese name of the type.
                """
                return self._data.get("jp")
        return Name(self._data.get("name"))
    
    @property
    def sprites(self):
        """ The sprites of the type.

        Returns:
            Sprites: The sprites of the type.
        """
        return self._data.get("sprites")
    
    @property
    def resistances(self):
        """ The resistances of the type.

        Returns:
            list[Resistance]: The resistances of the type.
        """
        class Resistance(_tyradex_object):
            @property
            def name(self):
                """ The name of the resistance.

                Returns:
                    str: The name of the resistance.
                """
                return self._data.get("name")
            
            @property
            def multiplier(self):
                """ The multiplier of the resistance.

                Returns:
                    float: The multiplier of the resistance.
                """
                return self._data.get("multiplier")
        return [Resistance(resistance_data) for resistance_data in self._data.get("resistances", [])]
    
    @property
    def pokemons(self):
        """ The pokemons of the type.

        Returns:
            list[Pokemon]: The pokemons of the type.
        """
        return [Pokemon(pokemon_data) for pokemon_data in self._data.get("pokemons", [])]