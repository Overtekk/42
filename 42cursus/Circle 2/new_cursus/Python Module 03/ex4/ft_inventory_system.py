def ft_inventory_system(inventory: dict, username: str) -> None:

    # === Show a player inventory ===

    player_data = inventory.get(username)

    if player_data is None:
        print(f"Error: Player '{username}' not found.")
        return None

    print(f"=== {username}'s Inventory ===")
    inv = player_data.get("inventory")
    inv_value = 0
    item_count = 0
    category_list = []

    for item_name, item_details in inv.items():
        type = item_details.get("type")
        rarity = item_details.get("rarity")
        quantity = item_details.get("quantity")
        price = item_details.get("price")
        print(f"{item_name} ({type}, {rarity}): {quantity}x @ {price} gold "
              f"each = {quantity * price} gold")
        inv_value = inv_value + (quantity * price)
        item_count = item_count + quantity

    # === Show summary of player inventory ===

    print(f"\nInventory value: {inv_value} gold")
    print(f"Item count: {item_count} items")

    for item_name, item_details in inv.items():
        type = item_details.get("type")
        quantity = item_details.get("quantity")
        string = f"{type}({quantity})"
        category_list.append(string)

    category_result = ", ".join(category_list)

    print(f"Categories: {category_result}")

    # === Make a transaction (prefab with Bob and 2 potions) ===

    print(f"\n=== Transaction: {username} gives Bob 2 potions ===")

    potion_data = inv.get("potion")
    player_bob = inventory.get("Bob")
    inv_bob = player_bob.get("inventory")
    potions_bob = inv_bob.get("potions")

    if potion_data.get("quantity", 0) >= 2:
        print("Transaction successful!\n")
    else:
        print("Transaction failed...\n")


if __name__ == "__main__":

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

    ft_inventory_system(players, "Alice")
