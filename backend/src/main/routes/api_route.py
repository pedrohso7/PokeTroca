import json
from flask import Blueprint, jsonify, request

# User Factory Import
from src.main.factory.user.list_user_account_factory import ListUserAccountFactory
from src.main.factory.user.list_user_inventory_factory import ListUserInventoryFactory
from src.main.factory.user.add_user_account_factory import AddUserAccountFactory
from src.main.factory.user.authenticate_user_factory import AuthenticateUserFactory

# Trade Factory Import
from src.main.factory.trade.add_trade_solicitations_factory import AddTradeSolicitationsFactory
from src.main.factory.trade.list_trade_solicitations_factory import ListTradeSolicitationsFactory
from src.main.factory.trade.refuse_exchange_factory import RefuseExchangeFactory
from src.main.factory.trade.trade_pokemon_factory import TradePokemonFactory

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.route("/api/get-users", methods=["GET"])
def getAllUsers():
  result = ListUserAccountFactory.makeListUserAccountFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/user/inventory", methods=["GET"])
def getUserInventory():
  result = ListUserInventoryFactory.makeListUserInventoryFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/user/create", methods=["POST"])
def createUser():
  result = AddUserAccountFactory.makeUserAccountFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/login", methods=["GET"])
def getUser():
  result = AuthenticateUserFactory.makeAuthenticateUserFactory(request.json["params"])
  return jsonify(result)

# Trade Routes
@api_routes_bp.route("/api/trade/solicitations", methods=["GET"])
def getTradeSolicitation():
  result = ListTradeSolicitationsFactory.makeListTradeSolicitationsFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/trade/create", methods=["POST"])
def createTradeSolicitation():
  result = AddTradeSolicitationsFactory.makeAddTradeSolicitationsFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/trade/refuse", methods=["PUT"])
def refuseTradeSolicitation():
  result = RefuseExchangeFactory.makeRefuseExchangeFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/trade/accept", methods=["PUT"])
def tradePokemon():
  result = TradePokemonFactory.makeTradePokemonFactory(request.json["params"])
  return jsonify(result)