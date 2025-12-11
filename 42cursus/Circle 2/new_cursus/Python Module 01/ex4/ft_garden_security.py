def ft_garden_security():
    class SecurePlant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def get_info(self):
            print(f"{self.name} ({self.height}cm, {self.age} days)")

        def set_height(self, new_height):
            if (new_height < 0):
                print("Invalid operation attempted: height", end=" ")
                print(f"{self.height} [REJECTED]")
            else:
                self.height = new_height
                print(f"Height updated: {self.height}cm [OK]")

        def set_age(self, new_age):
            if (new_age < 0):
                print("Invalid operation attempted: age", end=" ")
                print(f"{self.age} [REJECTED]")
            else:
                self.age = new_age
                print(f"Age updated: {self.age} days [OK]")

        def get_height(self):
            if (self.height < 0):
                print("Security: Negative height rejected")
            else:
                print(f"Height updated: {self.height}cm [OK]")

        def get_age(self):
            if (self.age < 0):
                print("Security: Negative age rejected")
            else:
                print(f"Age updated: {self.age} days [OK]\n")

        def check_security(self):
            print(f"Plant created: {self.name}")
            plant.get_height()
            plant.get_age()

    plant = SecurePlant("Rose", 25, 30)

    print("=== Plant Security System ===")
    plant.check_security()
    plant.set_height(5)
    plant.set_age(-30)
    print("\nCurrent plant:", end=" ")
    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
