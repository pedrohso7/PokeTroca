from src.domain.usecases.user.list_user_inventory import ListUserInventory as ListUserInventoryInterface

class DbListUserInventory(ListUserInventoryInterface):
  
  def __init__(self, list_user_inventory_repository):
    self.list_user_inventory_repository = list_user_inventory_repository

  def get (self, id):
    return self.list_user_inventory_repository.get(id)