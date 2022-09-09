import sqlite3

con = sqlite3.connect('escambo.db', check_same_thread=False)

# Inserir informações POST
def insertTrade(body):
  with con:
    cur = con.cursor()
    query = "INSERT INTO 'Trade' (received_user_id, sender_user_id, want_pokemon_id, give_pokemon_id, status) VALUES (?, ?, ?, ?, ?)"
    cur.execute(query, (body['received_user_id'], body['sender_user_id'], body['want_pokemon_id'], body['give_pokemon_id'], 'pending'))

# Recupera todas as informações GET
def listTradeWithoutStatusFinished(id):
  tradeList = []
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'Trade' AS t INNER JOIN pokemon AS p ON p.id = t.want_pokemon_id INNER JOIN pokemon AS p1 ON p1.id = t.give_pokemon_id INNER JOIN user AS u ON u.id = t.sender_user_id INNER JOIN user AS u1 ON u1.id = t.received_user_id WHERE status LIKE 'pending' AND received_user_id = {id} AND sender_user_id <> {id} ORDER BY id ASC"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      tradeList.append(data)
  return tradeList

# Atualiza uma informações PUT
def tradePokemon(body, id):
  result = None
  with con:
    cur = con.cursor()
    query = f"UPDATE inventorypokemon SET pokemon_id = {body['want_pokemon_id']} WHERE inventory_id = {id} AND pokemon_id = {body['give_pokemon_id']}"
    cur.execute(query)
  return result

def secondTradePokemon(body, id):
  result = None
  with con:
    cur = con.cursor()
    query = f"UPDATE inventorypokemon SET pokemon_id = {body['give_pokemon_id']} WHERE inventory_id = {id} AND pokemon_id = {body['want_pokemon_id']}"
    cur.execute(query)
  return result

# Atualiza uma informações PUT
def updateTradeStatus(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"UPDATE trade SET status = 'finished' WHERE id = {id}"
    cur.execute(query)
  return result

def getOneSolicitation(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM trade WHERE id = {id}"
    cur.execute(query)
    result = cur.fetchone()
  return result



