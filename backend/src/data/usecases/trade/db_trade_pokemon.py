from src.domain.usecases.trade.trade_pokemon import TradePokemon as TradePokemonInterface

class DbTradePokemon(TradePokemonInterface):
  
  def __init__(self, trade_pokemon_repository):
    self.trade_pokemon_repository = trade_pokemon_repository

  def update (self, tradeData):
    return self.trade_pokemon_repository.update(tradeData)