import random
from src.infra.database.sqlite.views.inventory_pokemon.inventory_pokemon_view import *
from src.infra.database.sqlite.views.pokemon.pokemon_view import *
from src.infra.database.sqlite.views.user.user_view import *
from src.infra.database.sqlite.views.inventory.inventory_view import *
from src.data.protocols.user.add_user_account_repository import AddUserAccountRepository as AddUserAccountRepositoryInterface

class AddUserAccountRepo(AddUserAccountRepositoryInterface):
  
  def add(self, accountUserData):
    insert_user_result = insert(accountUserData)
    if (insert_user_result != None):
      return insert_user_result
    user_result = getLastUser()
    insertInventory(user_result[0])
    inventory_result = getLastInventory()
    for i in range(10):
      num = random.randint(1, 150)
      body = { "inventory_id": inventory_result[0], "pokemon_id": num }
      print('body', body)
      insertInventoryPokemon(body)
