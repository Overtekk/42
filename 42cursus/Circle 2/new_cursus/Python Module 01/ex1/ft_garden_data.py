class Plant:
    """Plant model with NAME, HEIGHT and AGE"""

    def __init__(self, *, name: str, height: int, days: int) -> None:
        """Initialize a plant"""

        self.name = name
        self.height = height
        self.days = days

    def display_info(self) -> str:
        """Return a string about plant information"""

        return f"{self.name}: {self.height}cm, {self.days} days old"


def ft_garden_data():
    """Create data for plants and print them"""

    plant_list = [
        Plant(name="Rose", height=25, days=30),
        Plant(name="Sunflower", height=80, days=45),
        Plant(name="Cactus", height=15, days=120)
    ]

    print("=== Garden Plant Registry ===")
    for data in plant_list:
        print(f"{data.display_info()}")


if __name__ == "__main__":
    ft_garden_data()
