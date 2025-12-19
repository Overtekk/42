# *==============================================*
# |            CUSTOM EXCEPTION CLASS            |
# *==============================================*

class GardenError(Exception):
    """Basic error for garden problems.
    Inherits from the built-in 'Exception' class or one of its subclasses.
    """

    pass


class PlantError(GardenError):
    """Catch error with watering.
    Inherits from GardenErrors
    """

    pass


class WaterError(GardenError):
    """Catch error with watering.
    Inherits from GardenErrors
    """

    pass


# *==============================================*
# |               PLANT CLASS                    |
# *==============================================*

class Plant():
    """Plant model with NAME"""

    def __init__(self, *, name: str, water_level: int,
                 sun_level: int, watered: bool, rotten: bool) -> None:
        """Initialize plant"""

        self.name = name
        self.water_level = water_level
        self.sun_level = sun_level
        self.watered = watered
        self.rotten = rotten


# *==============================================*
# |            GARDEN MANAGER CLASS              |
# *==============================================*


class GardenManager():
    """Main class that manage plants and check errors"""

    def __init__(self) -> None:
        """Initialize Manager"""

        self.garden = []

    def add_to_garden(self, *, plant: Plant) -> None:
        """Add plants to garden ONLY if name is correct"""

        try:
            if plant.name is None:
                raise ValueError
        except ValueError:
            print("Error adding plant: Plant name cannot be empty!")
        else:
            self.garden.append(plant)
            print(f"Added {plant.name} successfully")

    def water_plant(self) -> None:
        """Check if plant have been watered or not"""

        print("Watering plants...")
        print("Opening watering system")

        try:
            for plant in self.garden:
                try:
                    if plant.watered is True:
                        raise WaterError(f"{plant.name} have already been "
                                         "watered")
                    else:
                        print(f"Watering {plant.name} - success")
                        plant.water_level += 1
                except WaterError as e:
                    print(f"Caught {e.__class__.__name__}: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Check if a plant have good condition:
        - Water Level between 1 and 10
        - Sunlight Hours between 2 and 12
        """

        print("Checking plant health...")

        for plant in self.garden:
            try:
                if plant.water_level > 10:
                    raise ValueError(f"Water level {plant.water_level} is too "
                                     "hight (max 10)")
                if plant.water_level < 1:
                    raise ValueError(f"Water level {plant.water_level} is too "
                                     "low (min 1)")
                if plant.sun_level > 12:
                    raise ValueError(f"Sunlight hours {plant.sun_level} is too"
                                     " hight (max 12)")
                if plant.sun_level < 2:
                    raise ValueError(f"Sunlight hours {plant.sun_level} is too"
                                     " low (min 2)")
                if plant.rotten is True:
                    raise PlantError("plant have rotten. Oh no :(")
            except (ValueError, PlantError) as e:
                print(f"Error checking {plant.name}: {e}")
            else:
                print(f"{plant.name}: healthy (water: {plant.water_level}, "
                      f"sun: {plant.sun_level})")

    def error_recovery(self, *, water_tank: int, rats: int) -> None:
        """Test some other errors"""

        error = False

        try:
            if water_tank < 20:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
            error = True
        else:
            print("Tank have enough water")

        try:
            if rats > 0:
                raise GardenError("OMG. Rats are eating plants!!!!")
        except GardenError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
            error = True
        else:
            print("No rats in the garden. Good")

        if error is True:
            print("System recovered and continuing...")
        else:
            print("System all good...")


# *==============================================*
# |               MAIN FUNCTION                  |
# *==============================================*

def ft_garden_management() -> None:
    """Main function"""

    manager = GardenManager()

    plant_list = [
        Plant(name="tomato", water_level=5, sun_level=8, watered=False,
              rotten=False),
        Plant(name="lettuce", water_level=15, sun_level=3, watered=True,
              rotten=False),
        Plant(name=None, water_level=0, sun_level=8, watered=True,
              rotten=False),
        Plant(name="carrot", water_level=5, sun_level=0, watered=True,
              rotten=False),
        Plant(name="papaya", water_level=8, sun_level=6, watered=False,
              rotten=True)
    ]
    water_in_tank = 14  # max tank value: 20
    number_of_rats = 0

    print("=== Garden Management System ===\n")

    # === Add plants to garden ===

    for plant in plant_list:
        manager.add_to_garden(plant=plant)

    # === Water plants in garden ===

    print("")
    manager.water_plant()

    # === Check plant health ===

    print("")
    manager.check_plant_health()

    # === Check error recovery ===

    print("")
    manager.error_recovery(water_tank=water_in_tank, rats=number_of_rats)

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    ft_garden_management()
