class Plant:
    """Plant model with NAME, HEIGHT and AGE"""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initialize a plant"""

        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a string about plant information"""

        return f"{self.name} ({self.height}cm, {self.age} days)"


def ft_plant_factory():
    """Create plant quickly using Plant class"""

    count = 0
    plant_list = [
        Plant(name="Rose", height=25, age=30),
        Plant(name="Oak", height=200, age=365),
        Plant(name="Cactus", height=5, age=90),
        Plant(name="Sunflower", height=80, age=45),
        Plant(name="Fern", height=15, age=120)
    ]

    print("=== Plant Factory Output ===")
    for data in plant_list:
        print("Created:", end=" ")
        new_plant = data
        print(new_plant.get_info())
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
