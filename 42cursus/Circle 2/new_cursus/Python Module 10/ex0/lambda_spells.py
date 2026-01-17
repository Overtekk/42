def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda item: item['power'], reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = filter(lambda item: ())
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
    for item in sorted:
        print(f"{item['name']} ({item['power']} power)", end=" comes before ")

    print("\n\nTesting power filter...")
    mage_list = [
        {'name': 'Gérard le Gris', 'power': 66, 'element': 'fire'},
        {'name': 'Remy l\'Ignoble', 'power': 42, 'element': 'mud'},
        {'name': 'Francois le Géant', 'power': 500, 'element': 'rock'},
        {'name': 'Monoco himself', 'power': 2, 'element': 'feets'},
        {'name': 'Doggo the Dog', 'power': 12, 'element': 'bone'}
    ]
    filtered = power_filter(mage_list, 42)
    for item in filtered:
        print(f"{item['name']}", end=" - ")


if __name__ == "__main__":
    main()
