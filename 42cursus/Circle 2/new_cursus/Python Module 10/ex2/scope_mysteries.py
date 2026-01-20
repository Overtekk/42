def mage_counter() -> callable:
    count = 0

    def mage_counter2() -> int:
        nonlocal count
        count += 1
        return count
    return mage_counter2


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def spell2(power_add: int) -> int:
        nonlocal total
        total += power_add
        return total
    return spell2


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    mem = {}

    def store(key: str, value: any) -> None:
        mem.update({key: value})

    def recall(key: str) -> dict[str]:
        if mem.get(key) is None:
            return "Memory not found"
        return mem[key]
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    mage_count = mage_counter()
    for i in range(1, 10):
        print(f"Call {i}: {mage_count()}")

    print("\nTesting spell accumulator...")
    initial_power = 42
    power_to_add = 150
    spell = spell_accumulator(initial_power)
    print(f"Initial power: {initial_power}\nPower to add {power_to_add}")
    for i in range(1, 10):
        print(f"Call {i}: {spell(power_to_add)}")

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Fire aspect")
    knockback_enchant = enchantment_factory("Knockback")
    sharpness_enchant = enchantment_factory("Sharpness V")
    print(fire_enchant("Iron Sword"))
    print(knockback_enchant("Stick"))
    print(sharpness_enchant("Netherite Sword"))

    print("\nTesting memory vault...")
    memory = memory_vault()
    memory['store']('test', 42)
    print(memory['recall']('test'))
    print(memory['recall']('none'))


if __name__ == "__main__":
    main()
