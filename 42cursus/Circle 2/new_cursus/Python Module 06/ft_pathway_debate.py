import os
import alchemy
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life

print("=== Pathway Debate Mastery ===\n")

filename = os.path.basename(alchemy.transmutation.basic.__file__)
print(f"Testing Absolute Imports (from {filename})")

print(f"{lead_to_gold.__name__}(): {lead_to_gold()}")
print(f"{stone_to_gem.__name__}(): {stone_to_gem()}")

filename = os.path.basename(alchemy.transmutation.advanced.__file__)
print(f"\nTesting Relative Imports (from {filename})")

print(f"{philosophers_stone.__name__}(): {philosophers_stone()}")
print(f"{elixir_of_life.__name__}(): {elixir_of_life()}")

print("\nTesting Package Access:")

print(f"{alchemy.transmutation.__name__}."
      f"{alchemy.transmutation.lead_to_gold.__name__}(): "
      f"{alchemy.transmutation.lead_to_gold()}")
print(f"{alchemy.transmutation.__name__}."
      f"{alchemy.transmutation.philosophers_stone.__name__}(): "
      f"{alchemy.transmutation.philosophers_stone()}")

print("\nBoth pathways work! Absolute: clear, Relative: concise")
