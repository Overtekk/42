def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda item: item['power'], reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = filter(lambda item: (item['power'] >= min_power), mages)
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


def main() -> None:
    print("\nTesting artifact sorter...")
    artifact_list = [
        {'name': 'Goblin Crown', 'power': 5, 'type': 'legendary'},
        {'name': 'Mana Ring', 'power': 4, 'type': 'common'},
        {'name': 'Great Staff', 'power': 10, 'type': 'common'},
        {'name': 'Sea Best', 'power': 1, 'type': 'common'},
        {'name': 'Magic Keyboard', 'power': 52, 'type': 'coder'}
    ]
    sorted = artifact_sorter(artifact_list)
    msg = [f"'{item['name']}' ({item['power']} power)" for item in sorted]
    msg = " come before ".join(msg)
    print(msg)

    print("\n\nTesting power filter...", end="")
    min_power = 42
    print(f"(>= {min_power})")
    mage_list = [
        {'name': 'Gérard le Gris', 'power': 66, 'element': 'fire'},
        {'name': 'Remy l\'Ignoble', 'power': 42, 'element': 'mud'},
        {'name': 'Francois le Géant', 'power': 500, 'element': 'rock'},
        {'name': 'Monoco himself', 'power': 2, 'element': 'feets'},
        {'name': 'Doggo the Dog', 'power': 12, 'element': 'bone'}
    ]
    filtered = power_filter(mage_list, min_power)
    msg = [f"'{item['name']}' ({item['power']} power)"
               for item in filtered]
    msg = " - ".join(msg)
    print(msg)

    print("\nTesting spell transformer...")
    spell_list = ["Fireball", "Nuclear", "Kiss", "Heal", "Shield"]
    transform = spell_transformer(spell_list)
    print(transform)

if __name__ == "__main__":
    main()
