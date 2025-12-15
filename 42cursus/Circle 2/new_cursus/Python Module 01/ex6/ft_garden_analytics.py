class Plant:
    """Init Plant class"""
    def __init__(self, name, height):
        self.name = name
        self.height = height

    """Display general information about plant"""
    def get_info(self):
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Init Flower class (child of Plant class)"""
    def __init__(self, name, height, color, can_bloom):
        super().__init__(name, height)
        self.color = color
        self.can_bloom = can_bloom

    """Check if Flower can bloom"""
    def bloom(self):
        if self.can_bloom:
            return "(blooming)"
        else:
            return "(not blooming)"

    def get_info(self):
        base_info = super().get_info()
        return (f"{base_info} {self.color} flowers {self.bloom()}")


class PrizeFlower(FloweringPlant):
    """Init Prize for Flower class (child of Flower class)"""
    def __init__(self, name, height, color, is_bloom, prize):
        super().__init__(name, height, color, is_bloom)
        self.prize = prize


class GardenManager:
    """Manage all garden information"""
    class GardenStats:
        """Calculate stats of each garden"""
        def calculate(self, data):
            pass

    """Init class GardenManager"""
    def __init__(self):
        self.stats = self.GardenStats()
        self.gardens = {}

    """Create """
    @classmethod
    def create_garden_network(cls):
        pass

    """Create new plant and add it to the owner garden"""
    def add_plant(self, owner_name, plant_object):
        if owner_name not in self.gardens:
            self.gardens[owner_name] = []
        self.gardens[owner_name].append(plant_object)
        print(f"Added {plant_object.name} to {owner_name}'s garden")

    """Display garden information"""
    def get_info(self, owner_name):
        print(f"\n=== {owner_name}'s Garden Report ===\n")
        print("Plants in garden:")
        for plant in self.gardens[owner_name]:
            print(f"- {plant.get_info()}")


def ft_garden_analytics():
    """Manage multiple gardens, analyze informations and print all
    informations about them"""

    print("=== Garden Management System Demo ===\n")
    manager = GardenManager()
    garden_list_alice = [
        FloweringPlant("Rose", 26, "red", True),
        FloweringPlant("Sunflower", 51, "yellow", True)
    ]
    garden_list_romain = [
        FloweringPlant("Amaryllis", 23, "white", False),
        FloweringPlant("Chrysanthemum", 69, "pink", True)
    ]
    for data in garden_list_alice:
        manager.add_plant("Alice", data)
    for data in garden_list_romain:
        manager.add_plant("Romain", data)
    manager.get_info("Alice")


if __name__ == "__main__":
    ft_garden_analytics()
