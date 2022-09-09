from src.presentation.errors.errors import Errors

class ListUserAccountController:
  def __init__ (self, listUserAccount):
    self.listUserAccount = listUserAccount

  def list (self, socketRequest):
    print('SOCKET REQUEST', socketRequest)
    if socketRequest != {}:
      requiredFields = ["id"]

      for fields in requiredFields:
        if socketRequest[fields] == None:
          return Errors.badRequest(f"Missing {fields} Field")
      user_list = self.listUserAccount.get(socketRequest["id"])
      return Errors.ok(user_list)
    else:
      socketRequest = { "id": 5000 }
      user_list = self.listUserAccount.get(socketRequest["id"])
      return Errors.ok(user_list)