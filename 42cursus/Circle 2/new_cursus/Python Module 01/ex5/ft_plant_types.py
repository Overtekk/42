def ft_plant_types():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def get_info_plant(self):
            return f"{self.name}: {self.height}cm, {self.age} days"

    class Flower(Plant):
        def __init__(self, name, height, age, color, can_bloom):
            super().__init__(name, height, age)
            self.color = color
            self.can_bloom = can_bloom

        def get_info_flower(self):
            base_info = super().get_info_plant()
            return f"{base_info}, {self.color} color\n"

        def can_bloom():
            print("\nok")


    class Tree(Plant):
        def __init__(self, name, height, age, trunk_diameter, produce_shade):
            super().__init__(name, height, age)
            self.trunk_diameter = trunk_diameter
            self.produce_shade = produce_shade

    class Vegetable(Plant):
        def __init__(self, name, height, age, harvest_season,
                     nutritional_value):
            super().__init__(name, height, age)
            self.harvest_season = harvest_season
            self.nutrional_value = nutritional_value

    garden_list = []
    rose = Plant("Rose", 25, 30, "red", can_bloom())
    garden_list.append(rose)

    print("=== Garden Plant Types ===")
    for data in garden_list:
        print(data.get_info())

if __name__ == "__main__":
    ft_plant_types()
