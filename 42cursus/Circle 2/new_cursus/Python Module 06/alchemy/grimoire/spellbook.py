# === Late Import (import inside the function)===
def record_spell(spell_name: str, ingredients: str) -> str:
    """Save a spell using a name and alid ingredients.

    === Args ===
        - spell_name (str): The name of the spell to create.
        - ingredients (str): The list of ingredients to create the spell.
    """

    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)

    if "INVALID" not in result:
        return (f"Spell recorded: {spell_name} "
                f"({validate_ingredients(ingredients)})")
    return (f"Spell rejected: {spell_name} "
            f"({validate_ingredients(ingredients)})")

# === Dependency Injection (import as parameters) ===
# from typing import Callable


# def record_spell(spell_name: str, ingredients: str,
#                  validator_func: Callable) -> str:
#     """Save a spell using a name and alid ingredients.

#     === Args ===
#         - spell_name (str): The name of the spell to create.
#         - ingredients (str): The list of ingredients to create the spell.
#         - validator_func (function): The function to use to validate inputs.
#     """

#     result = validator_func(ingredients)

#     if "INVALID" not in result:
#         return f"Spell recorded: {spell_name} ({result})"
#     return f"Spell rejected: {spell_name} ({result})"
