class Plant:
    """Init slass"""
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    """Display informations about plant"""
    def get_info(self, curr_day):
        print(f"{self.name}: {self.height}cm, {self.days} days old")
        if curr_day > 1:
            print(f"Growth this week: +{self.total}cm")

    """Update growth size"""
    def grow(self, growth_size):
        self.total = growth_size
        self.height += growth_size

    """Update day"""
    def age(self, days_passed):
        self.days += days_passed


def ft_plant_growth():
    """Simulate a week of growth for plant"""

    plant_one = Plant("Rose", 25, 30)

    curr_day = 1

    print(f"=== Day {curr_day} ===")
    plant_one.get_info(curr_day)

    day_passed = 6
    curr_day += day_passed

    print(f"=== Day {curr_day} ===")

    growth_amount = 1 * day_passed

    plant_one.grow(growth_amount)
    plant_one.age(day_passed)
    plant_one.get_info(curr_day)


if __name__ == "__main__":
    ft_plant_growth()
