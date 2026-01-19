def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda item: (item['power'] >= min_power), mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda x: '* ' + x + ' *', spells)


def mage_stats(mages: list[dict]) -> dict:
    if len(mages) == 0:
        return None
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(sum(map(lambda x: x['power'], mages))
                           / len(mages), 2),
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifact_list = [
        {'name': 'Goblin Crown', 'power': 5, 'type': 'legendary'},
        {'name': 'Mana Ring', 'power': 4, 'type': 'common'},
        {'name': 'Great Staff', 'power': 10, 'type': 'common'},
        {'name': 'Sea Best', 'power': 1, 'type': 'common'},
        {'name': 'Magic Keyboard', 'power': 52, 'type': 'coder'}
    ]
    sorted_artifact = artifact_sorter(artifact_list)
    msg_sorted = [f"'{item['name']}' ({item['power']} power)"
                  for item in sorted_artifact]
    msg_sorted = " come before ".join(msg_sorted)
    print(msg_sorted)

    print("\nTesting power filter...", end="")
    min_power = 42
    print(f"(>= {min_power})")
    mage_list = [
        {'name': 'Gérard le Gris', 'power': 66, 'element': 'fire'},
        {'name': 'Remy l\'Ignoble', 'power': 42, 'element': 'mud'},
        {'name': 'Francois le Géant', 'power': 500, 'element': 'rock'},
        {'name': 'Monoco himself', 'power': 2, 'element': 'feets'},
        {'name': 'Doggo the Dog', 'power': 12, 'element': 'bone'}
    ]
    filtered_mage = power_filter(mage_list, min_power)
    msg_filtered = [f"'{item['name']}' ({item['power']} power)"
                    for item in filtered_mage]
    msg_filtered = " - ".join(msg_filtered)
    print(msg_filtered)

    print("\nTesting spell transformer...")
    spell_list = ["Fireball", "Nuclear", "Kiss", "Heal", "Shield"]
    transform_spell = spell_transformer(spell_list)
    msg_spell = [f"{item}" for item in transform_spell]
    msg_spell = " ".join(msg_spell)
    print(msg_spell)

    print("\nTesting mage stats...")
    stats = mage_stats(mage_list)
    print(stats)


if __name__ == "__main__":
    main()
