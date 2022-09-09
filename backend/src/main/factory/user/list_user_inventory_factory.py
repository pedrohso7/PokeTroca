from src.presentation.controllers.user.list_user_inventory import ListUserInventoryController
from src.data.usecases.user.db_list_user_inventory import DbListUserInventory
from src.infra.database.sqlite.repository.list_user_inventory_repository.list_user_inventory import ListUserInventoryRepo

class ListUserInventoryFactory:
  def makeListUserInventoryFactory(socketRequest):
    listUserInventoryRepo = ListUserInventoryRepo()
    dbListUserInventory = DbListUserInventory(listUserInventoryRepo)
    listUserInventoryController = ListUserInventoryController(dbListUserInventory)
    result = listUserInventoryController.list(socketRequest)
    return result