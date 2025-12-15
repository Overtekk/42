class Plant:
    """Init class"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    """Display information about plant"""
    def get_info(self):
        print(f"{self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory():
    """Create plant quickly"""

    count = 0
    plant_list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for data in plant_list:
        print("Created:", end=" ")
        new_plant = Plant(data[0], data[1], data[2])
        new_plant.get_info()
        count += 1
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
