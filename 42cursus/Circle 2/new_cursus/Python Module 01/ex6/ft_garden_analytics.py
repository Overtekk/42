# +------------------------------------------------------------+
# |                       Plant Class                          |
# +------------------------------------------------------------+

class Plant:
    """Plant model with only NAME and HEIGHT"""

    def __init__(self, *, name: str, height: int) -> None:
        """Initialize a plant"""

        self.name = name
        self.height = height

    def grow(self, *, increment: int = 1) -> None:
        """Grow a plant by incrementing 1cm"""

        self.height += increment

    def get_info(self) -> str:
        """Return a string about plant information"""

        return f"{self.name}: {self.height}cm"


# +------------------------------------------------------------+
# |                     Flowering Plant Class                  |
# +------------------------------------------------------------+


class FloweringPlant(Plant):
    """Flowering plant with COLOR and bool: CAN_BLOOM"""

    def __init__(self, *, name: str, height: int, color: str,
                 can_bloom: bool) -> None:
        """Initialize flowering flower"""

        super().__init__(name=name, height=height)
        self.color = color
        self.can_bloom = can_bloom

    def bloom(self) -> str:
        """Check if a flower can bloom"""

        if self.can_bloom:
            return "(blooming)"
        else:
            return "(not blooming)"

    def get_info(self) -> str:
        """Return a string about plant information"""

        base_info = super().get_info()
        return (f"{base_info} {self.color} flowers {self.bloom()}")


# +------------------------------------------------------------+
# |                     Prize Flower Class                     |
# +------------------------------------------------------------+


class PrizeFlower(FloweringPlant):
    """Prize flower with POINTS"""

    def __init__(self, *, name: str, height: int, color: str,
                 can_bloom: bool, prize: int) -> None:
        """Initialize prize flower"""

        super().__init__(name=name, height=height, color=color,
                         can_bloom=can_bloom)
        self.prize = prize

    def get_info(self) -> str:
        """Return a string about plant information"""

        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize}"


# +------------------------------------------------------------+
# |                     Garden Manager                         |
# +------------------------------------------------------------+


class GardenManager:
    """Manage multiples gardens with nested statistics helper"""

    def __init__(self) -> None:
        """Initialize manager"""

        self.gardens = {}

    class GardenStats:
        """Helper for stats of a garden (nested inside GardenManager)"""

        def __init__(self, *, name: str) -> None:
            """Initialize stats"""

            self.name = name
            self.plants = ()
            self.added = 0
            self.count_regular = 0
            self.count_flowering = 0
            self.count_prized = 0
            self.total_growth = 0

        def count_plant_type(self, *, plant_type: str) -> None:
            """Count each plant type"""

            if plant_type == "PrizeFlower":
                self.count_prized += 1
            if plant_type == "FloweringPlant":
                self.count_flowering += 1
            if plant_type == "Plant":
                self.count_regular += 1

    """Static Method because it's an utility function. It don't take self
    (object), neither cls (class). It's here because we need it for
    garden logical"""
    @staticmethod
    def check_height(height: int) -> bool:
        """Check if a plant height is valid (non negative value)"""

        if height >= 0:
            return True
        else:
            return False

    """Class Method, like a factory. It take the class (clc) and can create
    a new GardenManager with cls()"""
    @classmethod
    def create_garden_network(cls):
        """Create pre-constructed garden"""

        manager = cls()
        manager.gardens["Alice"] = []
        manager.gardens["Bob"] = []
        return manager

    def add_plant(self, *, garden_name: str, plant: Plant) -> None:
        """Add plant to a specific garden ONLY if it's valid"""

        if garden_name not in self.gardens:
            print(f"Error: Garden {garden_name} not found")
            return

        if self.check_height(plant.height) is True:
            print(f"Added {plant.name} to {garden_name}'s garden")
            self.gardens[garden_name].append(plant)
        else:
            print(f"Cannot add {plant.name} to {garden_name}'s garden because"
                  f" {plant.height} is invalid")

    def water_garden(self, *, garden_name: str) -> None:
        """Add 1 to height of each plant of a specific garden"""
        if garden_name not in self.gardens:
            print(f"Error: Garden {garden_name} not found")
            return

        plant_list = self.gardens[garden_name]
        print(f"\n{garden_name} is helping all plants grow...")
        for plant in plant_list:
            plant.height += 1
            print(f"{plant.name} grew 1cm")

    def get_garden_report(self, *, garden_name: str) -> str:
        """Display summary of a specific garden"""

        if garden_name not in self.gardens:
            return "\nError: Garden not found"

        header = f"\n=== {garden_name}'s Garden Report ==="

        plant_list = self.gardens[garden_name]

        if not plant_list:
            return header + "\nNo plants in this garden"

        stats = self.GardenStats(name=garden_name)

        plant_info = "\nPlants in garden:"

        height_ok = True
        for plant in plant_list:
            if not self.check_height(plant.height):
                height_ok = False
                break

        for plant in plant_list:
            plant_info += f"\n- {plant.get_info()}"
            class_name = type(plant).__name__
            stats.count_plant_type(plant_type=class_name)
            stats.added += 1
            stats.total_growth += 1

        text = (
            f"\nPlants added: {stats.added}, "
            f"Total growth: {stats.total_growth}cm\n"
            f"Plant types: {stats.count_regular} regular, "
            f"{stats.count_flowering} flowering, "
            f"{stats.count_prized} prize flowers\n\n"
            f"Height validation test: {height_ok}"
        )

        return header + plant_info + "\n" + text

    def get_network_summary(self) -> None:
        """Display a summary of gardens network"""

        print("Garden scores -", end=" ")

        score = ""
        is_first = True
        for name in self.gardens:
            curr_score = 0
            for plant in self.gardens[name]:
                curr_score += plant.height
                class_name = plant.__class__.__name__
                if class_name == "PrizeFlower":
                    curr_score += plant.prize
                if (class_name == "FloweringPlant" or class_name
                        == "PrizeFlower"):
                    if plant.can_bloom is True:
                        curr_score += 15
            entry = f"{name}: {curr_score}"
            if is_first:
                score = entry
                is_first = False
            else:
                score += ", " + entry

        count = 0
        for i in self.gardens:
            count += 1

        print(f"{score}")
        print(f"Total gardens managed: {count}")


# +------------------------------------------------------------+
# |                     Main Function                          |
# +------------------------------------------------------------+


def ft_garden_analytics() -> None:
    """Main function for managing multiple gardens"""

    manager = GardenManager.create_garden_network()

    garden_list_alice = [
        Plant(name="Oak Tree", height=100),
        FloweringPlant(name="Rose", height=25, color="red", can_bloom=True),
        PrizeFlower(name="Sunflower", height=50, color="yellow",
                    can_bloom=True, prize=10)
    ]
    garden_list_bob = [
        FloweringPlant(name="Amaryllis", height=23, color="white",
                       can_bloom=False),
        FloweringPlant(name="Chrysanthemum", height=69, color="pink",
                       can_bloom=False),
        Plant(name="Cactus", height=-1)
    ]

    print("=== Garden Management System Demo ===\n")

    for data in garden_list_alice:
        manager.add_plant(garden_name="Alice", plant=data)
    for data in garden_list_bob:
        manager.add_plant(garden_name="Bob", plant=data)

    manager.water_garden(garden_name="Alice")

    print(manager.get_garden_report(garden_name="Alice"))
    manager.get_network_summary()


if __name__ == "__main__":
    ft_garden_analytics()
