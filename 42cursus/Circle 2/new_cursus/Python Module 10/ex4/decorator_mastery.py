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
            if args[0] >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return valid_power
    return decorator


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


@spell_timer
def fireball() -> str:
    return 'Fireball cast'

@power_validator
def power(n: int) -> int:
    return n


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    print(f"Result: {power(10)}")


if __name__ == "__main__":
    main()
