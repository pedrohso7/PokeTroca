import sqlite3
import sys
import traceback

con = sqlite3.connect('escambo.db', check_same_thread=False)

# Inserir informações POST
def insert(body):
  with con:
    cur = con.cursor()
    query = "INSERT INTO user (email, password, name) VALUES (?, ?, ?)"
    try:
      cur.execute(query, (body['username'], body['password'], body['name']))
      con.commit()
      result = cur.fetchone()
      return result
    except sqlite3.Error as er:
      msg = ' '.join(er.args)
      return msg

# Recupera todas as informações GET
def list(id):
  userList = []
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' WHERE id <> {id} ORDER BY name ASC"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      userList.append(data)
  return userList

def listWithoutId():
  userList = []
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' ORDER BY name ASC"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      userList.append(data)
  return userList

# Recupera uma informações GET
def getOne(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' WHERE id = {id}"
    cur.execute(query)
    result = cur.fetchone()
  return result

  # Recupera uma informações GET
def getLastUser():
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' ORDER BY id DESC LIMIT 1"
    cur.execute(query)
    result = cur.fetchone()
  return result

# Recupera uma informações GET
def authenticate(body):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' WHERE email = '{body['username']}' AND password = '{body['password']}'"
    print('query', query)
    cur.execute(query)
    result = cur.fetchone()
  return result
