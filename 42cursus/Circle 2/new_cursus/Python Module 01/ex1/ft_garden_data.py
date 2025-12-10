def ft_garden_data():
    class Plant:
        def ___init___(self, name, height, days):
            self.name = name
            self.height = height
            self.days = days

    plant_one = Plant('Rose', 25, 30)
    plant_two = Plant('Sunflower', 80, 45)
    plant_three = Plant('Cactus', 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{plant_one}")


if __name__ == "__main__":
    ft_garden_data()
