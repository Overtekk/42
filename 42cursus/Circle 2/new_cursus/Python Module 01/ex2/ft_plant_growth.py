def ft_plant_growth():
    class Plant:
        def __init__(self, name, height, days):
            self.name = name
            self.height = height
            self.days = days

        def get_info(self):
            print(f"{self.name}: {self.height}cm, {self.days} days old")
            if curr_day > 1:
                print(f"Growth this week: +{self.total}cm")

        def grow(self, growth_size):
            self.total = growth_size
            self.height += growth_size
            # self.total = self.height
            # self.height += curr_day
            # self.total = self.height - self.total

        def age(self, days_passed):
            self.days += days_passed

    plant_one = Plant("Rose", 25, 30)

    curr_day = 1
    print(f"=== Day {curr_day} ===")
    plant_one.get_info()

    day_passed = 6
    curr_day += day_passed

    print(f"=== Day {curr_day} ===")

    growth_amount = 1 * day_passed

    plant_one.grow(growth_amount)
    plant_one.age(day_passed)
    plant_one.get_info()


if __name__ == "__main__":
    ft_plant_growth()
