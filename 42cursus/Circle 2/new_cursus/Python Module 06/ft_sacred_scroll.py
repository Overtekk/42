import os
import alchemy


print("=== Sacred Scroll Mastery ===\n")
print("Testing direct module access:")

func_fire = alchemy.elements.create_fire
func_water = alchemy.elements.create_water
func_earth = alchemy.elements.create_earth
func_air = alchemy.elements.create_air

print(f"{func_fire.__module__}.{func_fire.__name__}(): {func_fire()}")
print(f"{func_water.__module__}.{func_water.__name__}(): {func_water()}")
print(f"{func_earth.__module__}.{func_earth.__name__}(): {func_earth()}")
print(f"{func_air.__module__}.{func_air.__name__}(): {func_air()}")

filename = os.path.basename(alchemy.__file__)
print(f"\nTesting package-level access (controlled by {filename})")

func_list = ["create_fire", "create_water", "create_earth", "create_air"]

for name in func_list:
    print(f"{alchemy.__name__}.{name}()", end=": ")
    try:
        func = getattr(alchemy, name)
        print(func())
    except AttributeError:
        print("AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
