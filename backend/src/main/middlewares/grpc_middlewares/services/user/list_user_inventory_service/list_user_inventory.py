from urllib import response

from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2
from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2_grpc
from src.main.factory.user.list_user_inventory_factory import ListUserInventoryFactory

class ListUserInventoryService(list_user_inventory_pb2_grpc.ListUserInventoryServicer):
    def makeListUserInventoryFactory(self, request, context):
        print('REQUEST', request)
        new_request = {
            "id": request.id
        }
        result = ListUserInventoryFactory.makeListUserInventoryFactory(new_request)
        if (result['statusCode'] == 400):
            response = list_user_inventory_pb2.Response(statusCode = result['statusCode'], message = result['body']['msg'])
            return response
        array_pokemon = []
        for pokemon in result['body']['inventory_data']:
            poke = list_user_inventory_pb2.Inventory(pokemonid = pokemon['pokemon_id'], pokemonname = pokemon['pokemon_name'], pokemonimage = pokemon['pokemon_image'])
            array_pokemon.append(poke)
        response = list_user_inventory_pb2.Response(
            statusCode = result['statusCode'],
            userid = result['body']['user_id'],
            username = result['body']['user_name'],
            inventoryid = result['body']['iventory_id'],
            inventories = array_pokemon,
        )
        return response