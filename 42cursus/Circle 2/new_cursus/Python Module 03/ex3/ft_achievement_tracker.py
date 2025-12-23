def ft_achievement_tracker(achievements: list) -> None:
    """Build a achievement tracker and analytics.

    === Arguments ===
        - List with achievements name

    === Returns ===
        - None: This function only prints to stdout

    This function take a list with achievements name inside. We give to each
    player some achievements and then analyse all unique achievements (no
    duplicated name), and achievements common to all players and more.
    We learn how to use sets, differences, union and intersection.
    """

    print("=== Achievement Tracker System ===\n")

    alice_success = [achievements[0], achievements[2], achievements[3],
                     achievements[5]]
    bob_success = [achievements[0], achievements[2], achievements[4],
                   achievements[-1]]
    charlie_success = [achievements[2], achievements[3], achievements[4],
                       achievements[5], achievements[6]]

    set_alice = set(alice_success)
    set_bob = set(bob_success)
    set_charlie = set(charlie_success)

    print(f"Player alice achievements: {set_alice}")
    print(f"Player bob achievements: {set_bob}")
    print(f"Player charlie achievements: {set_charlie}")

    print("\n=== Achievement Analytics ===")

    unique_achievement = set(achievements)
    print(f"All unique achievements: {unique_achievement}")
    print(f"Total unique achievements: {len(unique_achievement)}")

    common_success = set_alice.intersection(set_bob, set_charlie)
    # or you can use set_alice & set_bob & set_charlie
    print(f"\nCommon to all players: {common_success}")

    alice_only = set_alice.difference(set_bob.union(set_charlie))
    bob_only = set_bob.difference(set_alice.union(set_charlie))
    charlie_only = set_charlie.difference(set_alice.union(set_bob))
    rare_success = alice_only.union(bob_only, charlie_only)
    print(f"Rare achievement (1 player): {rare_success}")

    # we don't check Charlie achievements here
    print(f"\nAlice vs Bob common: {set_alice.intersection(set_bob)}")
    print(f"Alice unique: {set_alice.difference(set_bob)}")
    print(f"Bob unique: {set_bob.difference(set_alice)}")


if __name__ == "__main__":
    """
    Here, we create a simple list of achievements and give it to the
    function.
    """

    achievement_list = [
        "first_kill",
        "first_kill",
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
        "collector"
    ]

    ft_achievement_tracker(achievements=achievement_list)
