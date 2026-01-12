from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard
from ex0.CreatureCard import CreatureCard


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
    fire_dragon = TournamentCard("Fire Dragon", 6, "Legendary", 6, 7, 3,
                                 "dragon_001")
    ice_wizard = TournamentCard("Ice Wizard", 5, "Rare", 4, 12, 1,
                                "wizard_001")

    print(tournament.register_card(fire_dragon))
    print(tournament.register_card(ice_wizard))
    print("")

    get_card_info(fire_dragon)
    print("")
    ice_wizard.elo = 1150
    get_card_info(ice_wizard)

    print("\nCreating tournament match...")
    print("")

    print("Match result: "
          f"{tournament.create_match('dragon_001', 'wizard_001')}")

    print(f"\nPlatform Report:\n{tournament.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
