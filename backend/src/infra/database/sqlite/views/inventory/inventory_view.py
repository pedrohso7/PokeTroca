import sqlite3

con = sqlite3.connect('escambo.db', check_same_thread=False)

# Inserir informações POST
def insertInventory(id):
  with con:
    cur = con.cursor()
    query = "INSERT INTO inventory (user_id) VALUES (?)"
    cur.execute(query, (id, ))

# Recupera todas as informações GET
def listInventory():
  inventoryList = []
  with con:
    cur = con.cursor()
    query = "SELECT * FROM 'Inventory'"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      inventoryList.append(data)
  return inventoryList

# Recupera uma informações GET
def getLastInventory():
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'Inventory' ORDER BY id DESC LIMIT 1"
    cur.execute(query)
    result = cur.fetchone()
  return result

def getInventoryAndUserData(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT i.id, u.id, u.name FROM 'Inventory' AS i INNER JOIN user AS u ON u.id = i.user_id WHERE user_id = {id}"
    cur.execute(query)
    result = cur.fetchone()
  return result

