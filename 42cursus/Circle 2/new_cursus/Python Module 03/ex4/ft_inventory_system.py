def ft_inventory_system(inventory: dict, username: str) -> None:
    """Build an inventory system and do some checks.

    === Arguments ===
        - Inventory: a dictionnary containing all the data (dict)
        - Username: the username of the player we want to show (str)

    === Returns ===
        - None: This function only prints to stdout or stop if player
                doesn't exist

    Here, we learn how to use dictionnaries. First, we show the all
    inventory of the player we want (except if it doesn't exist). Then, we
    do a transaction between 2 players and update there inventory.
    """

    # =======================================
    # |       Show a player inventory       |
    # =======================================

    player_data = inventory.get(username)

    # If player doesn't exist, return None
    if player_data is None:
        print(f"Error: Player '{username}' not found.")
        return None

    print(f"=== {username}'s Inventory ===")

    inv = player_data.get('inventory')
    inv_value = 0
    item_count = 0
    category_list = []

    # Boucle to get player inventory and print it
    for item_name, item_details in inv.items():
        type = item_details.get('type')
        rarity = item_details.get('rarity')
        quantity = item_details.get('quantity')
        price = item_details.get('price')
        print(f"{item_name} ({type}, {rarity}): {quantity}x @ {price} gold "
              f"each = {quantity * price} gold")
        inv_value = inv_value + (quantity * price)
        item_count = item_count + quantity

    # Show more informations from player inventory
    print(f"\nInventory value: {inv_value} gold")
    print(f"Item count: {item_count} items")

    for item_name, item_details in inv.items():
        type = item_details.get('type')
        quantity = item_details.get('quantity')
        string = f"{type}({quantity})"
        category_list.append(string)

    category_result = ", ".join(category_list)
    print(f"Categories: {category_result}")

    # ===============================================
    # |     Make a transaction between 2 players    |
    # |       (prefab with Bob and n potions)       |
    # ===============================================

    potions_transa = 2  # You can choose how many potions to give

    print(f"\n=== Transaction: {username} gives Bob {potions_transa} "
          "potions ===")

    # Check if player have enought potions to perform the trade
    if inv['potion']['quantity'] >= potions_transa:
        print("Transaction successful!\n")

        inv['potion']['quantity'] -= potions_transa

        player_bob = inventory.get('Bob')  # Get player Bob
        inv_bob = player_bob.get('inventory')  # Get Bob inventory
        potions_data_bob = inv_bob.get('potion')  # Get Bob potion category

        # If 'potion' don't exist for Bob, we create it and update Bob inv
        if potions_data_bob is None:
            create_potions_categ_bob = {
                "potion": {"type": "consumable", "rarity": "common",
                           "quantity": 0, "price": 50},
            }
            inv_bob.update(create_potions_categ_bob)
            potions_data_bob = inv_bob['potion']

        potions_data_bob['quantity'] += potions_transa

        print("=== Updated Inventories ===")
        print(f"{username} potions: {inv['potion']['quantity']}")
        print(f"Bob potions: {inv_bob['potion']['quantity']}")

    else:
        print("Transaction failed...")

    # =======================================
    # |      Get inventory's analytic       |
    # =======================================
    print("\n=== Inventory Analytics ===")

    max_value = 0
    max_item = 0
    best_player_value = None
    best_player_item = None
    rare_item = []

    for player, player_data in inventory.items():
        player_inv = player_data.get('inventory')
        current_total_value = 0
        current_total_item = 0

        for item_name, item_details in player_inv.items():
            quantity = item_details.get('quantity')
            price = item_details.get('price')

            current_total_value = current_total_value + (quantity * price)
            current_total_item = current_total_item + quantity

            if "rare" in item_details.get('rarity'):
                rare_item.append(item_name)

        if current_total_value > max_value:
            max_value = current_total_value
            best_player_value = player

        if current_total_item > max_item:
            max_item = current_total_item
            best_player_item = player

    print(f"Most valuable player: {best_player_value} ({max_value} golds)")
    print(f"Most items: {best_player_item} ({max_item} items)")
    print(f"Rarest items: {', '.join(rare_item)}")


if __name__ == "__main__":
    """Create inventory using dict().

    This function create a dictionaries 'players' containing multiple
    players. Each player have is own inventory with items, and each item
    have multiple value inside.
    We send this dictionnarie to the ft_inventory_system() function.
    """

    print("=== Player Inventory System ===\n")

    players = {
        "Alice": {
            "inventory": {
                "sword": {"type": "weapon", "rarity": "rare", "quantity": 1,
                          "price": 500},
                "potion": {"type": "consumable", "rarity": "common",
                           "quantity": 5, "price": 50},
                "shield": {"type": "armor", "rarity": "uncommon",
                           "quantity": 1, "price": 200}
            }
        },
        "Bob": {
            "inventory": {
                "magic_ring": {"type": "weapon", "rarity": "rare",
                               "quantity": 1, "price": 500},
            }
        },
    }

    ft_inventory_system(inventory=players, username="Alice")
