from src.infra.database.sqlite.views.user.user_view import *
from src.infra.database.sqlite.views.pokemon.pokemon_view import *
from src.infra.database.sqlite.views.inventory.inventory_view import *
from src.data.protocols.user.list_user_inventory_repository import ListUserInventoryRepository as ListUserInventoryRepositoryInterface

class ListUserInventoryRepo(ListUserInventoryRepositoryInterface):
  
  def get (self, id):
    inventory_info = getInventoryAndUserData(id)
    if (inventory_info == None):
      return None
    user_inventory_result = getPokemonsInInventory(inventory_info[0])
    if (user_inventory_result == None):
      return None
    user_inventory_dict = {
      "user_id": inventory_info[1],
      "user_name": inventory_info[2],
      "iventory_id": inventory_info[0],
      "inventory_data": []
    }
    for item in user_inventory_result:
      user_inventory_dict["inventory_data"].append(
        { 
          "pokemon_id": item[1],
          "pokemon_name": item[2],
          "pokemon_image": item[3]
        }
      )
    return user_inventory_dict