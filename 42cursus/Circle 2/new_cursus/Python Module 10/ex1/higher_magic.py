def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    # def power(target):
    #     result_original = base_spell(target)
    #     result_final = result_original * multiplier
    #     return result_final
    # return power

    return lambda x: (base_spell(x) * multiplier)


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda x: spell(x) if condition(x) is True else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda x: [spell(x) for spell in spells]


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(lambda target: f"Fireball hits {target}",
                              lambda target: f"Heals {target}")
    result_combined = combined("Dragon")
    print(f"Combined spell result: {result_combined[0]}, {result_combined[1]}")

    print("\nTesting power amplifier...")

    def original(s: any) -> int:
        return 10
    amplified = power_amplifier(original, 3)
    print(f"Original: {original('test')}, Amplified: {amplified('test')}")

    print("\nTesting conditional caster...")

    def condition(n: int) -> bool:
        if n % 2 == 0:
            return True
        return False
    conditional = conditional_caster(condition, lambda target: "Fireball")
    print(f"Spell: {conditional(10)}\nSpell: {conditional(7)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([lambda target: f"Fireball hits {target}",
                               lambda target: f"Heals {target}",
                               lambda target: f"Missile explode {target}",
                               lambda target: f"Revive {target}",
                               lambda target: f"Flower poisonned {target}"])
    print(sequence("Remy"))


if __name__ == "__main__":
    main()
