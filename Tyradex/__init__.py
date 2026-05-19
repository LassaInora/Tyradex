with open("metadata.json", encoding="utf-8") as f:
    _METADATA = json.load(f)

_HEADERS = {
    "User-Agent": f"TyradexForPython/{_METADATA['version']}",
    "Content-type": "application/json"
}

class _Cache:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.sem = 604800  # 60 * 60 * 24 * 7
        self.root = Path.home() / ".tyradex"
        self.root.mkdir(exist_ok=True)
        self.path = self.root / f"{endpoint}.json"

        if self.path.exists():
            with open(self.path, "r") as f:
                try:
                    self.raw = json.load(f)
                except json.JSONDecodeError:
                    self.raw = None
        else:
            self.raw = None
    
    @property
    def valid(self):
        """ Vérifie si le cache est encore valide en fonction de sa date de création et du délai de validité (sem). """
        if self.raw is not None:
            return time.time() - self.raw.get("timestamp", 0) < self.sem
        else:
            return False

    @property
    def data(self):
        """ Retourne les données du cache si elles sont valides, sinon None. """
        if self.valid:
            return self.raw.get("data")
        else:
            return None
    
    @data.setter
    def data(self, value):
        """ Met à jour les données du cache et enregistre le cache dans un fichier. """
        self.raw = {
            "timestamp": time.time(),
            "data": value
        }
        with self.path.open("w") as f:
            json.dump(self.raw, f)

class TyradexError(Exception):
    pass

class _Tyradex:
    API_URL = NotImplemented
        

    def _request(self, method, endpoint, force=False, **kwargs):
        """ Effectue une requête à l'API Tyradex.

        Args:
            method (str): La méthode HTTP à utiliser (GET, POST, etc.).
            endpoint (str): L'endpoint de l'API à appeler.
            force (bool, optional): Si True, ignore le cache et effectue une nouvelle requête à l'API. Par défaut, False.
            **kwargs: Arguments supplémentaires à passer à la fonction requests.request().
        
        Returns:
            dict: La réponse de l'API sous forme de dictionnaire.
        """

        cache = _Cache(endpoint)
        if force or not cache.valid:
            url = f"{self.API_URL}/{endpoint}"
            headers = kwargs.pop("headers", {})
            headers.update(_HEADERS)

            response = requests.request(method, url, headers=headers, **kwargs)

            if not response.ok:
                raise TyradexError(f"API request failed with status code {response.status_code}: {response.text}")

            cache.data = response.json()
        
        return cache.data

class _TyradexV1(_Tyradex):
    API_URL = "https://tyradex.app/api/v1/"

    class Pokemon:
        @classmethod
        def pokedex(cls):
            """ Permet d'obtenir la liste de tous les Pokémons.
            
            Returns:
                list: Une liste de dictionnaires, chacun contenant les informations d'un Pokémon.
            """
            return [objects.v1.Pokemon(pokemon_data) for pokemon_data in cls._request("GET", f"pokemon")]
        
        @classmethod
        def pokemon(cls, name_or_id, region=None):
            """ Permet d'obtenir des informations sur un Pokémon spécifique.

            Args:
                name_or_id (str|int): Correspond à l'identifiant du Pokémon dans le Pokédex National ou son nom.
                region (str, optional): Correspond à la région du Pokémon. Permet de récupèrer les informations sur une forme régionale d'un Pokémon.
            
            Returns:
                dict: Un dictionnaire contenant les informations du Pokémon.
            """
            return objects.v1.Pokemon(cls._request("GET", f"pokemon/{name_or_id}{f'/{region}' if region else ''}"))
    
    class Generation:
        @classmethod
        def generations(cls):
            """ Permet d'obtenir la liste des différentes générations.
            
            Returns:
                list: Une liste de dictionnaires, chacun contenant les informations d'une génération.
            """
            return [objects.v1.Generation(gen_data) for gen_data in cls._request("GET", f"gen")]
        
        @classmethod
        def generation(cls, gen):
            """ Permet d'obtenir des informations sur une génération spécifique.

            Args:
                gen (int): Correspond au numéro de la génération.
            
            Returns:
                dict: Un dictionnaire contenant les informations de la génération.
            """
            return [objects.v1.Pokemon(pokemon_data) for pokemon_data in cls._request("GET", f"gen/{gen}")]

    class Types:
        @classmethod
        def types(cls):
            """ Permet d'obtenir la liste de tous les types.
            
            Returns:
                list: Une liste de dictionnaires, chacun contenant les informations d'un type de Pokémon.
            """
            return [objects.v1.Type(type_data) for type_data in cls._request("GET", f"types")]
        
        @classmethod
        def type(cls, type1, type2=None):
            """ Permet d'obtenir des informations sur un type spécifique.

            Args:
                type1 (str): Correspond à l'identifiant du type, ou bien son nom anglais ou français.
                type2 (str, optional): Correspond au deuxième type souhaité. Avec la combinaison, cela vous permet d'obtenir les Pokémons possédants ce double type.

            Returns:
                dict: Un dictionnaire contenant les informations sur le type de Pokémon.
            """
            return objects.v1.Type(cls._request("GET", f"types/{type1}{f'/{type2}' if type2 else ''}"))

    def __init__(self):
        super().__init__("https://tyradex.app/api/v1/")

class _TyradexV3(_Tyradex):
    API_URL = "https://tyradex.app/api/v3/"

class Tyradex(Enum):
    V1 = _TyradexV1
    V3 = _TyradexV3