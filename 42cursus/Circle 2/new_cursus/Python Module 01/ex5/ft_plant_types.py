import math


def ft_plant_types():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def get_info(self):
            type_name = self.__class__.__name__
            return (f"{self.name} ({type_name}): {self.height}cm, "
                    f"{self.age} days")

    class Flower(Plant):
        def __init__(self, name, height, age, color, can_bloom):
            super().__init__(name, height, age)
            self.color = color
            self.can_bloom = can_bloom

        def bloom(self):
            if self.can_bloom:
                return f"{self.name} is blooming beautifully!"
            else:
                return f"{self.name} is not blooming"

        def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, {self.color} color\n{self.bloom()}\n"

    class Tree(Plant):
        def __init__(self, name, height, age, trunk_diameter, produce_shade):
            super().__init__(name, height, age)
            self.trunk_diameter = trunk_diameter
            self.produce_shade = produce_shade

        def shade_area(self):
            if self.produce_shade:
                radius = self.height / 100
                area = math.pi * (radius ** 2)
                return (f"{self.name} provides {int(area)} "
                        "square meters of shade")
            else:
                return f"{self.name} do not provides shade"

        def get_info(self):
            base_info = super().get_info()
            return (f"{base_info}, {self.trunk_diameter}cm diameter\n"
                    f"{self.shade_area()}\n")

    class Vegetable(Plant):
        def __init__(self, name, height, age, harvest_season,
                     nutritional_value):
            super().__init__(name, height, age)
            self.harvest_season = harvest_season
            self.nutrional_value = nutritional_value

        def get_info(self):
            base_info = super().get_info()
            return (f"{base_info}, {self.harvest_season} harvest\n"
                    f"{self.name} is rich in {self.nutrional_value}\n")

    garden_list = [
        Flower("Rose", 25, 30, "red", True),
        Flower("Poppy", 10, 14, "yellow", False),
        Tree("Oak", 500, 1825, 50, True),
        Tree("Birch", 350, 1296, 41, False),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 5, 6, "summer", "vitamin A")
    ]

    print("=== Garden Plant Types ===\n")
    for data in garden_list:
        print(f"{data.get_info()}")


# if __name__ == "__main__":
#     ft_plant_types()
