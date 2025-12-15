def ft_seed_inventory(seed_types: str, quantity: int, unit: str):
    if ("packets" in unit):
        print(f"{seed_types.capitalize()} seeds: {quantity} {unit} available")
    elif ("grams" in unit):
        print(f"{seed_types.capitalize()} seeds: {quantity} {unit} total")
    elif ("area" in unit):
        print(f"{seed_types.capitalize()} seeds:", end=" ")
        print(f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
