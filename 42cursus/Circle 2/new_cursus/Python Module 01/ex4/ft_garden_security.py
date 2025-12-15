class SecurePlant:
    """Init class"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    """Display information about plant"""
    def get_info(self):
        print(f"{self.name} ({self.height}cm, {self.age} days)")

    """Set new height ONLY if it's valid"""
    def set_height(self, new_height):
        if (new_height < 0):
            print("Invalid operation attempted: height", end=" ")
            print(f"{self.height} [REJECTED]")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm [OK]")

    """Set new age ONLY if it's valid"""
    def set_age(self, new_age):
        if (new_age < 0):
            print("Invalid operation attempted: age", end=" ")
            print(f"{self.age} [REJECTED]")
        else:
            self.age = new_age
            print(f"Age updated: {self.age} days [OK]")

    """Check if starting height value is valid"""
    def get_height(self):
        if (self.height < 0):
            print("Security: Negative height rejected")
        else:
            print(f"Height updated: {self.height}cm [OK]")

    """Check if starting age value is valid"""
    def get_age(self):
        if (self.age < 0):
            print("Security: Negative age rejected")
        else:
            print(f"Age updated: {self.age} days [OK]\n")

    """Create plant and check if informations are valid"""
    def check_security(self, plant):
        print(f"Plant created: {self.name}")
        plant.get_height()
        plant.get_age()


def ft_garden_security():
    """Check valid plant information"""

    plant = SecurePlant("Rose", 25, 30)

    print("=== Plant Security System ===")
    plant.check_security(plant)
    plant.set_height(5)
    plant.set_age(-30)
    print("\nCurrent plant:", end=" ")
    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
