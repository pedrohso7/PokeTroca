from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from middleware_grpc import runGRPCMethod

class InventoryController():
    def __init__(self, **kwargs):
        super(InventoryController, self).__init__(**kwargs)
        
    def on_back_pressed(self):
        MDApp.get_running_app().root.transition.direction = 'right'
        MDApp.get_running_app().root.current = "Home"

    def get_user_inventory(self, id):
        params = {
            "id": id, 
        }
        res = runGRPCMethod( 'user/inventory', params)
        if(res.statusCode == 400):
            return Snackbar(text=res.message, bg_color=(1, 0, 0, 1),).open()
        return res.inventories

    def get_pokemon_index(self, pokemon_array, pokemon_name):
        pokemon_id = None
        for pokemon in pokemon_array:
            if(pokemon.pokemonname == pokemon_name):
                pokemon_id = pokemon.pokemonid
        return pokemon_id

    def create_barter(self, sender_id, receiver_id, want_pokemon, give_pokemon, my_pokemons, pokemons):
        def get_pokemon_index(pokemon_array, pokemon_name):
            pokemon_id = None
            for pokemon in pokemon_array:
                if(pokemon.pokemonname == pokemon_name):
                    pokemon_id = pokemon.pokemonid
            return pokemon_id
        pokemon_id = get_pokemon_index(pokemons, want_pokemon)
        my_pokemon_id = get_pokemon_index(my_pokemons, give_pokemon)

        if(pokemon_id == None):
            return Snackbar(text='Nome do pokemon que deseja incorreto', bg_color=(1, 0, 0, 1),).open()
        if(my_pokemon_id == None):
            return Snackbar(text='Nome do seu pokemon incorreto', bg_color=(1, 0, 0, 1),).open()

        params = {
            "sender_user_id": sender_id, 
            "received_user_id": receiver_id,
            "want_pokemon_id": pokemon_id,
            "give_pokemon_id": my_pokemon_id
        }
        res = runGRPCMethod( 'trade/create', params)
        if(res.statusCode == 400):
            return Snackbar(text=res.message, bg_color=(1, 0, 0, 1),).open()
        return Snackbar(text='Solicitação feita com sucesso', bg_color=(0, 1, 0, 1),).open()