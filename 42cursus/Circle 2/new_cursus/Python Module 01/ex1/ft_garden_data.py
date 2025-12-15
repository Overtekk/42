class Plant:
    """Init class"""
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    """Display information about plant"""
    def display_info(self):
        return (f"{self.name}: {self.height}cm, {self.days} days old")


def ft_garden_data():
    """Create data for plants and display them"""

    plant_list = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for data in plant_list:
        print(f"{data.display_info()}")


if __name__ == "__main__":
    ft_garden_data()
