import sqlite3

con = sqlite3.connect('escambo.db', check_same_thread=False)

# Inserir informações POST
def insertInventoryPokemon(body):
  with con:
    cur = con.cursor()
    query = "INSERT INTO inventorypokemon (inventory_id, pokemon_id) VALUES (?, ?)"
    cur.execute(query, (body['inventory_id'], body['pokemon_id']))

# Recupera todas as informações GET
# def listInventory():
#   inventoryList = []
#   with con:
#     cur = con.cursor()
#     query = "SELECT * FROM 'Inventory'"
#     cur.execute(query)
#     result = cur.fetchall()
#     for data in result:
#       inventoryList.append(data)
#   return inventoryList

# Recupera uma informações GET
def getSpecificInventory(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'InventoryPokemon' WHERE inventory_id = {id}"
    cur.execute(query)
    result = cur.fetchone()
  return result

