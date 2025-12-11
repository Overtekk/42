def ft_garden_data():
    class Plant:
        def __init__(self, name, height, days):
            self.name = name
            self.height = height
            self.days = days

        def display_info(self):
            print(f"{self.name}: {self.height}cm, {self.days} days old")

    plant_one = Plant("Rose", 25, 30)
    plant_two = Plant("Sunflower", 80, 45)
    plant_three = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant_one.display_info()
    plant_two.display_info()
    plant_three.display_info()


# if __name__ == "__main__":
#     ft_garden_data()
