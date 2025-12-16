import math


class Plant:
    """Plant model with only NAME, HEIGHT and AGE"""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initialize a plant"""

        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a string about plant information"""

        type_name = self.__class__.__name__
        return f"{self.name} ({type_name}): {self.height}cm, {self.age} days"


class Flower(Plant):
    """Flowering plant with COLOR and bool: CAN_BLOOM"""

    def __init__(self, *, name: str, height: int, age: int, color: str,
                 can_bloom: bool) -> None:
        """Initialize flowering flower"""

        super().__init__(name=name, height=height, age=age)
        self.color = color
        self.can_bloom = can_bloom

    def bloom(self) -> str:
        """Check if a flower can bloom"""

        if self.can_bloom:
            return f"{self.name} is blooming beautifully!"
        else:
            return f"{self.name} is not blooming"

    def get_info(self) -> str:
        """Return a string about plant information"""

        base_info = super().get_info()
        return f"{base_info}, {self.color} color\n{self.bloom()}"


class Tree(Plant):
    """Tree plant with TRUNK DIAMETER and PRODUCE SHADE"""

    def __init__(self, *, name: str, height: int, age: int,
                 trunk_diameter: int, produce_shade: bool) -> None:
        """Initialize tree"""

        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade = produce_shade

    def shade_area(self) -> str:
        """Check if Tree produce shade and calcule the radius"""

        if self.produce_shade:
            radius = self.height / 100
            area = math.pi * (radius ** 2)
            return (f"{self.name} provides {int(area)} "
                    "square meters of shade")
        else:
            return f"{self.name} do not provides shade"

    def get_info(self) -> str:
        """Return a string about plant information"""

        base_info = super().get_info()
        return (f"{base_info}, {self.trunk_diameter}cm diameter\n"
                f"{self.shade_area()}")


class Vegetable(Plant):
    """Vegetable plant with HARVEST SEASON and NUTRITIONAL VALUE"""

    def __init__(self, *, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize vegetable"""

        super().__init__(name=name, height=height, age=age)
        self.harvest_season = harvest_season
        self.nutrional_value = nutritional_value

    def get_info(self) -> str:
        """Return a string about plant information"""

        base_info = super().get_info()
        return (f"{base_info}, {self.harvest_season} harvest\n"
                f"{self.name} is rich in {self.nutrional_value}")


def ft_plant_types():
    """Create different type of plant"""

    garden_list = [
        Flower(name="Rose", height=25, age=30, color="red", can_bloom=True),
        Flower(name="Poppy", height=10, age=14, color="yellow",
               can_bloom=False),
        Tree(name="Oak", height=500, age=1825, trunk_diameter=50,
             produce_shade=True),
        Tree(name="Birch", height=350, age=1296, trunk_diameter=41,
             produce_shade=False),
        Vegetable(name="Tomato", height=80, age=90, harvest_season="summer",
                  nutritional_value="vitamin C"),
        Vegetable(name="Carrot", height=5, age=6, harvest_season="summer",
                  nutritional_value="vitamin A")
    ]

    print("=== Garden Plant Types ===\n")
    for data in garden_list:
        print(f"{data.get_info()}")
        print("")


if __name__ == "__main__":
    ft_plant_types()
