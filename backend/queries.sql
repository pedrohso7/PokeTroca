/*QUERIES PARA O CASO DE USO DE CADASTRO*/
    /*Query para cadastro de usuário*/
    INSERT INTO 'User' (email, name, password) VALUES ('teste@teste.com', 'teste', 'teste123')
    /*Query para criar inventario*/
    INSERT INTO 'Inventory' (id_user) VALUES (1)
    /*Query para criar pokemon*/
    INSERT INTO 'Pokemon' (name) VALUES ('pikachu')
    /*Query para criar inventario com pokemon*/
    INSERT INTO 'InventoryPokemon' (id_inventory, id_pokemon) VALUES (1, 1)

/*QUERIES PARA O CASO DE USO DE LOGIN*/
    /*Query para login*/
    SELECT * FROM 'User' WHERE email = 'teste@teste.com' AND password = 'teste123'

/*Query para lista de usuários*/
SELECT * FROM 'User' ORDER BY name ASC
/*Query para listar inventario de um usuário*/
SELECT * FROM 'Pokemon' AS p WHERE p.id IN (
    SELECT id_pokemon FROM 'InventoryPokemon' WHERE id_inventory = 1
)
/*Query para criar pedido de troca*/
INSERT INTO 'Trade' (id_received, id_sender, id_received_pokemon, id_sender_pokemon) VALUES (1, 2, 1, 2)
/*Query para listar pedidos de troca*/

