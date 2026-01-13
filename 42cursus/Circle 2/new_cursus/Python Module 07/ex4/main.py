from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard
import random


def get_card_info(card: TournamentCard) -> None:
    info = card.get_card_info()
    info_rank = card.get_rank_info()
    info_tournament = card.get_tournament_stats()
    print(f"{info['name']} (ID: {info['id']}):")
    print(f"Interfaces: {info['interfaces']}")
    print(f"Rating: {info_rank['elo']}")
    print(f"Record: {info_tournament['win']}-{info_tournament['losses']}")


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    tournament = TournamentPlatform()

    print(f"Platform Report:\n{tournament.generate_tournament_report()}")

    fire_dragon = TournamentCard("Fire Dragon", 6, "Legendary", 6, 7, 3,
                                 "dragon_001")
    ice_wizard = TournamentCard("Ice Wizard", 5, "Rare", 4, 12, 1,
                                "wizard_001")
    obelix = TournamentCard("Obelix", 10, "Unique", 1000, 800, 40, "obelix_01")
    duck = TournamentCard("The Greatest Duck", 3, "Legendary", 18, 18, 18,
                          "duck_01")
    remy = TournamentCard("Remy the Rat Slayer", 10, "Unique",
                          random.randint(1, 12), random.randint(1, 22),
                          random.randint(1, 10), "remy_01")
    manu = TournamentCard("Manu the trainer", 10, "Unique",
                          random.randint(1, 12), random.randint(1, 22),
                          random.randint(1, 10), "manu_01")
    rat = TournamentCard("Rat", 1, "Common", 1, 1, 1, "rat_01")

    my_cards = [fire_dragon, ice_wizard, obelix, duck, remy, manu, rat]
    ice_wizard.elo = 1150
    obelix.elo = 3012
    duck.elo = 404
    rat.elo = 10

    print("")
    for cards in my_cards:
        print(tournament.register_card(cards))
    print("")

    for cards in my_cards:
        get_card_info(cards)
        print("")

    participant_list = []
    hurted_list = []
    for cards in my_cards:
        hurted = random.randint(0, 10)
        if hurted == 2:
            print(f"Oh no.. {cards.name} has been hit by a car. He can't "
                  "participe in the tournament...")
            hurted_list.append(cards)
        else:
            participant_list.append(cards)

    for cards in hurted_list:
        tournament.unregister_card(cards)

    if len(hurted_list) > 0:
        print("")

    print("Creating tournament match...")
    try:
        for i in range(len(participant_list)):
            for j in range(i + 1, len(participant_list)):
                card1 = participant_list[i].id
                card2 = participant_list[j].id
                match = tournament.create_match(card1, card2)
                print(f"Match result: {match}")
    except ValueError as e:
        print(e)
        exit(2)

    print("\nTournament Leaderboard:")
    leader = tournament.get_leaderboard()
    for item in range(len(leader)):
        print(f"{item + 1}. {leader[item].name} - Rating: {leader[item].elo} "
              f"({leader[item].wins}-{leader[item].losses})")

    print(f"\nPlatform Report:\n{tournament.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
