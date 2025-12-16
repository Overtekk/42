class Plant:
    """Plant model with NAME, HEIGHT and AGE"""

    def __init__(self, *, name: str, height: int, days: int) -> None:
        """Initialize a plant"""

        self.name = name
        self.height = height
        self.days = days

    def get_info(self, *, curr_day: int) -> str:
        """Return a string about plant information"""

        plant_info = f"{self.name}: {self.height}cm, {self.days} days old"

        if curr_day > 1:
            growth_info = f"Growth this week: +{self.total}cm"
            return plant_info + "\n" + growth_info

        return plant_info

    def grow(self, *, growth_size: int) -> None:
        """Update growth size based on current day"""

        self.total = growth_size
        self.height += growth_size

    def age(self, *, days_passed: int) -> None:
        """Update day"""

        self.days += days_passed


def ft_plant_growth():
    """Simulate a week of growth for plant"""

    plant_one = Plant(name="Rose", height=25, days=30)

    curr_day = 1

    print(f"=== Day {curr_day} ===")
    print(plant_one.get_info(curr_day=curr_day))

    day_passed = 6
    curr_day += day_passed

    print(f"=== Day {curr_day} ===")

    growth_amount = 1 * day_passed

    plant_one.grow(growth_size=growth_amount)
    plant_one.age(days_passed=day_passed)
    print(plant_one.get_info(curr_day=curr_day))


if __name__ == "__main__":
    ft_plant_growth()
