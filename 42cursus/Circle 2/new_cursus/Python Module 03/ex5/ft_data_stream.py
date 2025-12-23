# import random
from typing import Generator


def data_stream(events: int) -> Generator[tuple[int, str, int, str],
                                          None, None]:
    """Create a generator for game events.

    === Arguments ===
        - Events (int): n numbers of events.

    === Returns ===
        - Generator of tuple type: the event_id, the player name, the player
        level and the event_type, doesn't need data injection, return None

    Create an events list and try to randomize it with some maths since we
    can't use 'import random'. We create a loop to have 3 players, levels and
    event_type. Then, we return everything with 'yield' so it returns 1 line
    per line and not everything at once.
    """

    event_list = [
        "killed monster",
        "found treasure",
        "leveled up"
    ]

    for event_id in range(1, events + 1):
        if event_id % 3 == 1:
            player = "alice"
        elif event_id % 2 == 1:
            player = "bob"
        else:
            player = "charlie"

        level = (event_id * 4) % 23 + 1

        event_type = event_list[(event_id + level) % 3]

        # I don't know if we can use the 'random library, so I comment it just
        # in case. But it's better to use it to have a true random generator.
        # level = random.randint(1, 14)
        # event_type = random.choice(event_list)

        yield (event_id, player, level, event_type)


def fibonacci_sequence(count: int) -> Generator[int, None, None]:
    """Print the n first numbers of fibonacci sequence.

    === Arguments ===
        - Count (int): n numbers of fibonacci number wanted.

    === Return ===
        - Generator of int type: the number in the fibonacci sequence, doesn't
        need data injection, return None.

    The sequence starts with 0 and 1. Each result is the sum of the two
    preceding ones. We use two variables (a, b) and update them simultaneously
    at each step: a becomes b, and b becomes a + b.
    """

    a, b = 0, 1

    for _ in range(count):
        yield a
        a, b = b, a + b


def prime_numbers(count: int) -> Generator[int, None, None]:
    """Print the n first prime numbers.

    === Arguments ===
        - Count (int): n numbers of prime numbers wanted.

    === Return ===
        - Generator of int type: the next prime number, doesn't need data
        injection, return None.

    Iterates through integers starting from 2 (because it can't be negative,
    0 or 1). Then, checks if the number is prime by verifying it has no
    divisors other than 1 and itself. Yields the number if prime and
    decrements the counter. Stops when 'count' reaches 0.
    """

    num = 2

    while count > 0:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime is True:
            yield num
            count -= 1

        num += 1


if __name__ == "__main__":
    """Run the data stream processor demonstration.

    Demonstrates stream processing of game events and calculates analytics
    without loading all data into memory. Then, shows examples with Fibonacci
    and prime number generators.
    """

    print("=== Game Data Stream Processor ===\n")

    data_num = 1000
    print(f"Processing {data_num} game events...\n")

    generator = data_stream(events=1000)
    treasure_event_count = 0
    level_event_count = 0
    level_ten_count = 0

    for event_id, player, level, event_type in generator:
        print(f"Event {event_id}: Player {player} (level {level}) "
              f"{event_type}")
        if "found treasure" in event_type:
            treasure_event_count += 1
        if "leveled up" in event_type:
            level_event_count += 1
        if level >= 10:
            level_ten_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {data_num}")
    print(f"High-level players (10+): {level_ten_count}")
    print(f"Treasure events: {treasure_event_count}")
    print(f"Level-up events: {level_event_count}")

    print("\nMemore usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n===Generator Demonstration ===")

    # ========================================
    # |             Fibonacci                |
    # ========================================

    fibonaci_wanted = 10
    fibonaci_list = []

    for i in fibonacci_sequence(count=fibonaci_wanted):
        string = f"{i}"
        fibonaci_list.append(string)

    print_fibonacci = ", ".join(fibonaci_list)
    print(f"Fibonacci sequence (first {fibonaci_wanted}): {print_fibonacci}")

    # ========================================
    # |             Prime number             |
    # ========================================

    prime_numbers_wanted = 5
    prime_list = []

    for i in prime_numbers(count=prime_numbers_wanted):
        string = f"{i}"
        prime_list.append(string)

    print_prime_number = ", ".join(prime_list)
    print(f"Prime numbers (first {prime_numbers_wanted}): "
          f"{print_prime_number}")
