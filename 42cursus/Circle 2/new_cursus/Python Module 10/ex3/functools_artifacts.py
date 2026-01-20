import functools
import operator
import time


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'add':
        # return functools.reduce(lambda x, y: x + y, spells)
        return functools.reduce(operator.add, spells)
    if operation == 'max':
        return functools.reduce(max, spells)
    if operation == 'min':
        return functools.reduce(min, spells)
    if operation == 'multiply':
        # return functools.reduce(lambda x, y: x * y, spells)
        return functools.reduce(operator.mul, spells)
    return 0


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire_enchant = functools.partial(base_enchantment, power=50,
                                     element='Fire')
    ice_enchant = functools.partial(base_enchantment, power=50,
                                    element='Ice')
    light_enchant = functools.partial(base_enchantment, power=50,
                                      element='Lightning')
    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': light_enchant,
    }


@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def spell(data):
        return f"Unkown spell type for {type(data)}"

    @spell.register(int)
    def _(damage: int) -> str:
        return f"Dealing {damage} damage"

    @spell.register(str)
    def _(element: str) -> str:
        return f"Enchanting with {element}"

    @spell.register(list)
    def _(spells: list[any]) -> str:
        return f"Launching {spells}"

    return spell


def base_enchantment(power: int, element: str, target: str):
    return {'power': power, 'element': element, 'target': target}


def main() -> None:
    print("\nTesting spell reducer (without operator)...")
    spells = [42, 1, 5, 2, 50]
    operations = ['max', 'min', 'multiply', 'add']
    print(f"Sum: {spell_reducer(spells, operations[-1])}")
    print(f"Product: {spell_reducer(spells, operations[2])}")
    print(f"Max: {spell_reducer(spells, operations[0])}")
    print(f"Min: {spell_reducer(spells, operations[1])}")
    print(f"Invalid: {spell_reducer(spells, 'banana')}")

    print("\nTesting partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(enchant['fire_enchant'](target="Goblin"))
    print(enchant['ice_enchant'](target="Goblin"))
    print(enchant['lightning_enchant'](target="Goblin"))

    print("\nTesting memoized fibonacci...")
    # hits = numbers already found
    # misses = number not found (program executing)
    # currsize = number stocked in the cache
    n = 10
    for i in range(5):
        begin = time.time()
        res = memoized_fibonacci(n)
        end = time.time()
        print(f"Tour {i} : Time taken: {end-begin:.7f} - Fib({n}): {res}")
        print(memoized_fibonacci.cache_info())
        n += 1
    print("-- Recalling --")
    n = 10
    for i in range(5):
        begin = time.time()
        res = memoized_fibonacci(n)
        end = time.time()
        print(f"Tour {i} : Time taken: {end-begin:.7f} - Fib({n}): {res}")
        print(memoized_fibonacci.cache_info())
        n += 1

    print("\nTesting spell dispatcher...")
    spell_lst = [41, 'Fire Aspect', 85, 10, 'Protection']
    spell_n = 10
    spell_str = 'Sharpness'
    spell_not_supp = {'test': 'test'}
    dispatch = spell_dispatcher()
    print(dispatch(spell_n))
    print(dispatch(spell_str))
    print(dispatch(spell_lst))
    print(dispatch(spell_not_supp))


if __name__ == "__main__":
    main()
