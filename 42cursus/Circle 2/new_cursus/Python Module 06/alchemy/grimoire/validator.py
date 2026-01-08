def validate_ingredients(ingredients: str) -> str:
    """Return a string if ingredients is in the list

    === Args ===
        - ingredients (str): The ingredients to valide
    """

    ingr = ingredients.split(" ")
    valid_ingredients = ["fire", "water", "earth", "air"]

    for item in ingr:
        if item not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
