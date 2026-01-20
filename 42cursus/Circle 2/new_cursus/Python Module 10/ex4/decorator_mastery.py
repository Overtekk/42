from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def timer(*args, **kwargs):
        begin = time.time()
        print(f"Casting {func.__name__}")
        result = func(*args, **kwargs)
        # time.sleep(1)
        end = time.time()
        exec_time = end - begin
        print(f"Spell completed in {exec_time:.07f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:

        @wraps(func)
        def valid_power(*args, **kwargs):
            power_value = None
            for arg in args:
                if isinstance(arg, int):
                    power_value = arg
                    break

            if power_value is not None:
                if power_value >= min_power:
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
        return valid_power
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def retry(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        print(f"Spell casting failed after {max_attempts} "
                              "attempts")
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str) or len(name) < 3:
            return False

        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power}"


@spell_timer
def fireball() -> str:
    return 'Fireball cast'


@power_validator(50)
def power(n: int) -> int:
    return n


@retry_spell(3)
def broken_spell():
    print("Trying...")
    raise ValueError("Fizzle!")


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    print(f"Result: {power(5), 'Fire'}")
    print(f"Result: {power(80), 'Fire'}")

    print("\nTesting retry spell...")
    broken_spell()

    print("\nTesting spell timer...")
    print(MageGuild.validate_mage_name("wizard"))
    print(MageGuild.validate_mage_name("wizard06"))
    print(MageGuild.validate_mage_name("wi"))
    print(MageGuild.validate_mage_name("wiz ard"))
    print(MageGuild.validate_mage_name("wiz06 ard"))
    print(MageGuild().cast_spell("Lightning", 15))
    print(MageGuild().cast_spell("Lightning", 9))


if __name__ == "__main__":
    main()
