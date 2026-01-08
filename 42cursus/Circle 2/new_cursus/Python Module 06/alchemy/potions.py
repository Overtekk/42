from alchemy import create_fire, create_water
import alchemy.elements


def healing_potion() -> str:
    """Function that return a simple string"""
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Function that return a simple string"""
    return (f"Strength potion brewed with {alchemy.elements.create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    """Function that return a simple string"""
    return (f"Invisibility potion brewed with {alchemy.elements.create_air()}"
            f" and {create_water()}")


def wisdom_potion() -> str:
    """Function that return a simple string"""
    return (f"Wisdom potion brewed with all elements: {create_fire} and "
            f"{create_water} and {alchemy.elements.create_earth()} and "
            f"{alchemy.elements.create_air}")
