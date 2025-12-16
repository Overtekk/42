class SecurePlant:
    """Plant model with  NAME, HEIGHT and AGE and security"""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initialize a plant with private variables"""

        self.__name = name
        self.__height = height
        self.__age = age

    def get_info(self) -> str:
        """Return a string about plant information"""

        if self.__height < 0 or self.__age < 0:
            return (f"[INVALID] {self.__name} ({self.__height}cm, "
                    f"{self.__age} days)")
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"

    def set_height(self, *, new_height: int) -> None:
        """Set new height ONLY if it's valid"""

        if (new_height < 0):
            print(f"Invalid operation attempted: height {new_height}cm "
                  "[REJECTED]")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, *, new_age: int) -> None:
        """Set new age ONLY if it's valid"""

        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> None:
        """Check if starting height value is valid"""

        if (self.__height < 0):
            print("Security: Negative height rejected")
        else:
            print(f"Height updated: {self.__height}cm [OK]")

    def get_age(self) -> None:
        """Check if starting age value is valid"""

        if (self.__age < 0):
            print("Security: Negative age rejected")
        else:
            print(f"Age updated: {self.__age} days [OK]")

    def check_security(self, *, plant: str) -> None:
        """Create plant and check if informations are valid"""

        print(f"Plant created: {self.__name}")
        plant.get_height()
        plant.get_age()


def ft_garden_security():
    """Check valid plant information"""

    plant = SecurePlant(name="Rose", height=25, age=-30)

    print("=== Plant Security System ===")
    plant.check_security(plant=plant)
    print("")

    plant.set_height(new_height=-5)
    plant.set_age(new_age=8)

    print("\nCurrent plant", end=": ")
    print(plant.get_info())


if __name__ == "__main__":
    ft_garden_security()
