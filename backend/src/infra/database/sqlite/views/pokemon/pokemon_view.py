import sqlite3

con = sqlite3.connect('escambo.db', check_same_thread=False)

# Inserir informações POST
def insertPokemon(body):
  with con:
    cur = con.cursor()
    query = "INSERT INTO pokemon (name) VALUES (?)"
    cur.execute(query, (body['name']))

# Recupera todas as informações GET
def listPokemon():
  pokemonList = []
  with con:
    cur = con.cursor()
    query = "SELECT * FROM 'Pokemon' ORDER BY name ASC"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      pokemonList.append(data)
  return pokemonList

# Recupera uma informações GET
def getOnePokemon(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'Pokemon' WHERE id = {id}"
    cur.execute(query)
    result = cur.fetchone()
  return result

# Recupera uma informações GET
def getPokemonsInInventory(id):
  result = None
  with con:
    cur = con.cursor()
    # "SELECT * FROM 'InventoryPokemon' AS ip INNER JOIN pokemon AS p ON p.id = ip.pokemon_id WHERE inventory_id = {id}"
    query = f"SELECT ip.inventory_id, p.id, p.name, p.image FROM 'InventoryPokemon' AS ip INNER JOIN pokemon AS p ON p.id = ip.pokemon_id WHERE inventory_id = {id}"
    cur.execute(query)
    result = cur.fetchall()
  return result

