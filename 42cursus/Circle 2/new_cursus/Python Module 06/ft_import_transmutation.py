import alchemy.elements
import alchemy.potions
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water

print("=== Import Transmutation Mastery ===")

print("\nMethod 1 - Full module import")
print(f"{alchemy.elements.__name__}.{alchemy.elements.create_fire.__name__}():"
      f" {alchemy.elements.create_fire()}")

print("\nMethod 2 - Specific function import:")
print(f"{create_water.__name__}(): "
      f"{create_water()}")

print("\nMethod 3: - Aliased imports:")
print(f"heal(): {heal()}")

print("\nMethod 4: - Multiple imports:")
print(f"{alchemy.elements.create_earth.__name__}(): "
      f"{alchemy.elements.create_earth()}")
print(f"{alchemy.create_fire.__name__}(): {create_fire()}")
print(f"{alchemy.potions.strength_potion.__name__}(): "
      f"{alchemy.potions.strength_potion()}")

print("\nAll import transmutation methods mastered!")
