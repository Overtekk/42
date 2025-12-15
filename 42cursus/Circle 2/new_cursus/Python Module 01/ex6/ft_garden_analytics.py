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

    def get_info(self):
        base_info = super().get_info()
        return (f"{base_info}, Prize points: {self.prize}")


class GardenManager:
    """Manage all garden information"""
    class GardenStats:
        """Calculate stats of each garden"""
        def get_stats(self, data):
            __count = 0
            for data in data:
                __count = __count + 1
            print(f"\nPlant added: {__count}, Total growth:")

        def get_scores(self, owner_name):
            print(f"Garden scores - {owner_name}: ")

        """Calculate how many gardens"""
        def get_total_gardens(self, data):
            __count = 0
            for data in data:
                __count = __count + 1
            print(f"Total gardens managed: {__count}")

    """Init class GardenManager"""
    def __init__(self):
        self.stats = self.GardenStats()
        self.gardens = {}

    """Create pre-constructed garden"""
    @classmethod
    def create_garden_network(cls):
        new_manager = cls()
        new_manager.gardens["Test"] = [
            FloweringPlant("Carnation", 2, "pink", False),
            FloweringPlant("Tulip", 2, "yellow", True)
        ]
        return new_manager

    """Check if a plant height is valid (non negative value)"""
    @staticmethod
    def check_height(height):
        if height >= 0:
            return True
        else:
            return False

    """Water all plants of a specific garden"""
    def water_plant(self, owner_name, plant_object):
        __count = 1;
        plant_object.height += __count
        print(f"{plant_object.name} grew {__count}cm")

    """Create new plant and add it to the owner garden"""
    def add_plant(self, owner_name, plant_object):
        if owner_name not in self.gardens:
            self.gardens[owner_name] = []
        if self.check_height(plant_object.height) is True:
            self.gardens[owner_name].append(plant_object)
            print(f"Added {plant_object.name} to {owner_name}'s garden")
        else:
            print(f"Cannot add {plant_object.name} to {owner_name}'s "
                  f"garden because height ({plant_object.height}) is invalid")

    """Display garden information"""
    def get_info(self, owner_name):
        print(f"\n=== {owner_name}'s Garden Report ===\n")
        print("Plants in garden:")
        for plant in self.gardens[owner_name]:
            print(f"- {plant.get_info()}")
        self.stats.get_stats(self.gardens[owner_name])
        self.stats.get_total_gardens(self.gardens)
        self.stats.get_scores(owner_name)


def ft_garden_analytics():
    """Manage multiple gardens, analyze informations and print all
    informations about them"""

    manager = GardenManager.create_garden_network()
    garden_list_alice = [
        Plant("Oak Tree", 101),
        FloweringPlant("Rose", 26, "red", True),
        PrizeFlower("Sunflower", 51, "yellow", True, 10)
    ]
    # garden_list_romain = [
    #     FloweringPlant("Amaryllis", 23, "white", False),
    #     FloweringPlant("Chrysanthemum", 69, "pink", True)
    # ]

    print("=== Garden Management System Demo ===\n")
    for data in garden_list_alice:
        manager.add_plant("Alice", data)
    # for data in garden_list_romain:
    #     manager.add_plant("Romain", data)
    for data in garden_list_alice:
        manager.water_plant("Alice", data)
    manager.get_info("Alice")


if __name__ == "__main__":
    ft_garden_analytics()
