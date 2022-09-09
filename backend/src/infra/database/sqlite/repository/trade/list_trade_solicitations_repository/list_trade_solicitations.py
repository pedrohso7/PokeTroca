from src.data.protocols.trade.list_trade_solicitations_repository import ListTradeSolicitationsRepository as ListTradeSolicitationsRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *

class ListTradeSolicitationsRepo(ListTradeSolicitationsRepositoryInterface):
  
  def get (self, id):
    trade_solicitation_result = listTradeWithoutStatusFinished(id)  
    if (trade_solicitation_result == None):
      return None
    trade_solicitation_dict = []
    for trade_data in trade_solicitation_result:
      trade_solicitation_dict.append(
        {
          "id": trade_data[0],
          "received_user_id": trade_data[1],
          "sender_user_id": trade_data[2],
          "want_pokemon_id": trade_data[3],
          "give_pokemon_id": trade_data[4],
          "status": trade_data[5],
          "want_pokemon_name": trade_data[7],
          "want_pokemon_image": trade_data[8],
          "give_pokemon_name": trade_data[10],
          "give_pokemon_image": trade_data[11],
          "received_user_name": trade_data[19],
          "sender_user_name": trade_data[15]
        }
      )
    return trade_solicitation_dict