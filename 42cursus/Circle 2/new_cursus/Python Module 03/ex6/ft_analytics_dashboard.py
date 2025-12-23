def list_comprehension(data: dict) -> str:
    """Demonstrate list comprehensions for filtering and transforming data.

    === Arguments ===
        - data (dict): A dictionary containing player information, including
          scores and active status.

    === Returns ===
        - str: A formatted string displaying the results of the list
        comprehensions (high scorers, doubled scores, and active players).

    This function applies three types of list comprehensions:
    1. Selects names of players with a score greater than 2000.
    2. Creates a new list with all scores multiplied by 2.
    3. Selects names of players where 'active' is True.
    """

    target_player = ["alice", "bob", "charlie", "diana"]

    hight_score = [name for name, info in data['player'].items()
                   if info['score'] > 2000 if name in target_player]

    score_doubled = [data['player'][name]['score'] * 2
                     for name in data['player'] if name in target_player]

    active_player = [name for name, active in data['player'].items()
                     if active['active'] is True if name in target_player]

    message = (
        f"High scorers (>2000): {hight_score}\n"
        f"Scores doubled: {score_doubled}\n"
        f"Active players: {active_player}"
    )

    return message


def dict_comprehension(data: dict) -> str:
    """Demonstrate dict comprehensions for creating mappings and grouping data.

    === Arguments ===
        - data (dict): A dictionary containing player information, including
          scores and active status.

    === Returns ===
        - str: A formatted string displaying the results of the dict
        comprehensions (scores, scores categories, and achievement counts).

    This function applies three types of dict comprehensions:
    1. Select target players to print score.
    2. Increase selected categories based on score.
    3. Count how many achievements target players have.
    """

    target_player = ["alice", "bob", "charlie"]

    player_score = {name: details['score']
                    for (name, details) in data['player'].items()
                    if name in target_player}

    score_categ = {
        "high": sum(
            1 for details in data['player'].values()
            if details['score'] >= 2000
            ),
        "medium": sum(
            1 for details in data['player'].values()
            if 1500 <= details['score'] < 2000
            ),
        "low": sum(
            1 for details in data['player'].values()
            if details['score'] < 1500
            ),
    }

    achievements_counts = {name: len(success_count['achievements'])
                           for (name, success_count) in data['player'].items()
                           if name in target_player}

    message = (
        f"Player scores: {player_score}\n"
        f"Score categories: {score_categ}\n"
        f"Achievement counts: {achievements_counts}"
    )

    return message


def set_comprehension(data: dict) -> str:
    """Demonstrate set comprehensions for finding unique values.

    === Arguments ===
        - data (dict): A dictionary containing player information, including
          scores and active status.

    === Returns ===
        - str: A formatted string displaying the results of the set
        comprehensions (unique players, unique achievements, and active
        regions).
    """

    target_player = ["alice", "bob", "charlie", "diana"]

    unique_player = {name for name in data['player']
                     if name in target_player}

    all_owned_achievements = [success for details in data['player'].values()
                              for success in details['achievements']]
    unique_success = {success for success in all_owned_achievements
                      if all_owned_achievements.count(success) == 1}

    active_regions = {region for details in data['player'].values()
                      for region in details['region']}

    message = (
        f"Unique players: {unique_player}\n"
        f"Unique achievements: {unique_success}\n"
        f"Active regions: {active_regions}"
    )

    return message


def ft_analytics_dashboard(data: dict) -> None:
    """Create an analytics dashboard using comprehensions.

    === Arguments ===
        - Data of a dict containing all informations

    === Returns ===
        - None: This function only print to stdout

    """

    print("===Game Analytics Dashboard ===\n")

    print("=== List Comprehension Exemples ===")
    print(f"{list_comprehension(data=data)}\n")

    print("===Dict Comprehension Examples ===")
    print(f"{dict_comprehension(data=data)}\n")

    print("===Set Comprehension Examples ===")
    print(f"{set_comprehension(data=data)}\n")


if __name__ == "__main__":

    data = {
        "player": {
            "alice": {
                "score": 2300,
                "active": True,
                "achievements": {"first_kill", "level_master",
                                 "we_need_to_go_deeper", "potions_master",
                                 "lover"},
                "region": "north"
            },
            "bob": {
                "score": 1800,
                "active": True,
                "achievements": {"level_10", "sky_limits", "catch_first_fish"},
                "region": "central"
            },
            "charlie": {
                "score": 2150,
                "active": True,
                "achievements": {"boss_slayer", "we_need_to_go_deeper",
                                 "potions_master", "sky_limits",
                                 "catch_first_fish", "find_a_grave",
                                 "kill_rat"},
                "region": "central"
            },
            "diana": {
                "score": 2050,
                "active": False,
                "achievements": {"level_master", "kill_rat", "find_a_grave"},
                "region": "east"
            },
            "remy": {
                "score": 1,
                "active": True,
                "achievements": {"your_first_mariage"},
                "region": "north"
            },
            "manu": {
                "score": 1692,
                "active": False,
                "achievements": {"your_first_mariage", "lover"},
                "region": "north"
            }
        },
        "achievements": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "we_need_to_go_deeper",
            "potions_master",
            "sky_limits",
            "catch_first_fish",
            "lover",
            "your_first_mariage",
            "find_a_grave",
            "kill_rat",
            "ft_printf"
        ]
    }

    ft_analytics_dashboard(data=data)
