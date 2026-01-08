from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Function that return a simple string"""
    return (f"Philosopher's stone created using {lead_to_gold()} and "
            f"{healing_potion()}")


def elixir_of_life() -> str:
    """Function that return a simple string"""
    return "Elixir of life: eternal youth achieved!"
