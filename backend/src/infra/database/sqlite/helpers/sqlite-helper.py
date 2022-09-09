import sqlite3
import requests
import json

con = sqlite3.connect('escambo.db')

with con:
  cur = con.cursor()
  cur.execute("CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL, name TEXT NOT NULL)")
  cur.execute("CREATE TABLE inventory (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES user(id))")
  cur.execute("CREATE TABLE pokemon (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, image TEXT)")
  cur.execute("CREATE TABLE trade (id INTEGER PRIMARY KEY AUTOINCREMENT, received_user_id INTEGER NOT NULL, sender_user_id INTEGER NOT NULL, want_pokemon_id INTEGER NOT NULL, give_pokemon_id INTEGER NOT NULL, status TEXT NOT NULL, FOREIGN KEY(received_user_id) REFERENCES user(id), FOREIGN KEY(sender_user_id) REFERENCES user(id), FOREIGN KEY(want_pokemon_id) REFERENCES pokemon(id), FOREIGN KEY(give_pokemon_id) REFERENCES pokemon(id))")
  cur.execute("CREATE TABLE inventorypokemon (id INTEGER PRIMARY KEY AUTOINCREMENT, inventory_id INTEGER NOT NULL, pokemon_id INTEGER NOT NULL, FOREIGN KEY(inventory_id) REFERENCES inventory(id), FOREIGN KEY(pokemon_id) REFERENCES pokemon(id))")

  for i in range(150):
    request_result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i+1}/")
    pokemon_data = json.loads(request_result.content)
    query = "INSERT INTO pokemon (name, image) VALUES (?, ?)"
    cur.execute(query, (pokemon_data["name"], pokemon_data["sprites"]["front_default"]))
# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()