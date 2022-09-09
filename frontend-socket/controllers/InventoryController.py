from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from client_socket import ClientSocket

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
        res = ClientSocket.req(self, 'user/inventory', params)
        if(res["statusCode"] == 400):
            return Snackbar(text=res['body']['msg'], bg_color=(1, 0, 0, 1),).open()
        return res["body"]["inventory_data"]

    def get_pokemon_index(self, pokemon_array, pokemon_name):
        pokemon_id = None
        for pokemon in pokemon_array:
            if(pokemon['pokemon_name'] == pokemon_name):
                pokemon_id = pokemon['pokemon_id']
        return pokemon_id

    def create_barter(self, sender_id, receiver_id, want_pokemon, give_pokemon, my_pokemons, pokemons):
        def get_pokemon_index(pokemon_array, pokemon_name):
            pokemon_id = None
            for pokemon in pokemon_array:
                if(pokemon['pokemon_name'] == pokemon_name):
                    pokemon_id = pokemon['pokemon_id']
            return pokemon_id
        # print('==========================================')
        # print({sender_id})
        # print({receiver_id})
        # print({want_pokemon})
        # print({give_pokemon})
        # print(my_pokemons)
        # print('==========================COLE========')
        # print(pokemons)
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
        res = ClientSocket.req(self, 'trade/create', params)
        if(res["statusCode"] == 400):
            return Snackbar(text=res['body']['msg'], bg_color=(1, 0, 0, 1),).open()
        return Snackbar(text='Solicitação feita com sucesso', bg_color=(0, 1, 0, 1),).open()