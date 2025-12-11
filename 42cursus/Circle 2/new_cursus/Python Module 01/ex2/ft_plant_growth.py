def ft_plant_growth():
    class Plant:
        def __init__(self, name, height, days, current_day, total):
            self.name = name
            self.height = height
            self.days = days
            self.current_day = current_day
            self.total = total

        def get_info(self):
            print(f"=== Day {self.current_day} ===")
            print(f"{self.name}: {self.height}cm, {self.days} days old")
            if self.current_day > 1:
                print(f"Growth this week: +{self.total}cm")

        def current_days(self):
            self.current_day += 6

        def grow(self):
            self.total = self.height
            self.height += 6
            self.total = self.height - self.total

        def age(self):
            self.days += 6

    plant_one = Plant("Rose", 25, 30, 1, 0)

    plant_one.get_info()
    plant_one.current_days()
    plant_one.grow()
    plant_one.age()
    plant_one.get_info()


# if __name__ == "__main__":
#     ft_plant_growth()
