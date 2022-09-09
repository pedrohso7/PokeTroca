from src.presentation.errors.errors import Errors

class ListUserInventoryController:
  def __init__ (self, listUserInventory):
    self.listUserInventory = listUserInventory

  def list (self, socketRequest):
    requiredFields = ["id"]

    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    user_inventory_list = self.listUserInventory.get(socketRequest["id"])
    return Errors.ok(user_inventory_list)