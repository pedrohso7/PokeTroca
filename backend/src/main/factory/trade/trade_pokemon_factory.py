from src.presentation.controllers.trade.trade_pokemon import TradePokemonController
from src.data.usecases.trade.db_trade_pokemon import DbTradePokemon
from src.infra.database.sqlite.repository.trade.trade_pokemon_repository.trade_pokemon import TradePokemonRepo

class TradePokemonFactory:
  def makeTradePokemonFactory(socketRequest):
    tradePokemonRepo = TradePokemonRepo()
    dbTradePokemon = DbTradePokemon(tradePokemonRepo)
    tradePokemonController = TradePokemonController(dbTradePokemon)
    result = tradePokemonController.handle(socketRequest)
    return result