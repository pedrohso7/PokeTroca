## Requisições e Respostas
1. Criar usuário
    Request: { "route": 'user/create', "params": { "username": 'teste2@teste.com', "password": '123teste', "name": 'teste' } }
    # Sucesso
        Response: { "statusCode": 200, body: {} }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

2. Login
    Request: { "route": 'login', "params": { "email": 'testee@teste.com', "password": '123teste' } }
    # Sucesso
        Response: { "statusCode": 200, body: { "id": 1, "username": 'teste', "name": 'samuel' }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

3. Recuperar lista de usuários
    Request: { "route": get-user, "params": {} }
    # Sucesso
        Response: { "statusCode": 200, body: {} }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

4. Recupera inventário do usuário
    Request: { "route": 'user/inventory', "params": { "id": 2 } }
    # Sucesso
        Response: { "statusCode": 200, body: { "user_id": 1, "user_name": '', "iventory_id": '' "inventory_data": [{ "pokemon_id": '', "pokemon_name": '', "pokemon_image": '' }] } }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

5. Recupera todas as solicitações de troca do usuário
    Request: { "route": 'trade/solicitations', "params": { "id": 2 } }
    # Sucesso
        Response: { "statusCode": 200, body: { 
          "received_user_id": '',
          "sender_user_id": ''
          "want_pokemon_id": ''
          "give_pokemon_id": ''
          "status": ''
          "want_pokemon_name": ''
          "want_pokemon_image": ''
          "give_pokemon_name": ''
          "give_pokemon_image": ''
          "received_user_name": ''
          "sender_user_name": '' 
        }}
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

6. Cria uma solicitação de troca
    Request: { "route": 'trade/create', "params": { "received_user_id": 3, "sender_user_id": 2, "want_pokemon_id": 64, 'give_pokemon_id': 32 } }
    # Sucesso
        Response: { "statusCode": 200, body: {} }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

7. Realiza uma troca
    Request: { "route": 'trade/accecpt', "params": { "id": 1 } }
    # Sucesso
        Response: { "statusCode": 200, body: {} }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }

8. Recusa uma troca
    Request: { "route": 'trade/refuse', "params": { "id": 2 } }
    # Sucesso
        Response: { "statusCode": 200, body: {} }
    # Error
        Response: { "statusCode": 400, body: { "msg": 'alguma msg' } }