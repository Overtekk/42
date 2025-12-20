import sys


def ft_score_analytics() -> None:
    """Processes and displays scores provided by the user.

    === Arguments ===
        - No arguments requiered

    === Returns ===
        - None: This function only prints to stdout

    This function only accept numbers provided by the user. Store
    them in a list and organize scores. Calculate the number of players, total
    score, average score, high score, low score and score range.
    """

    print("=== Player Score Analytics ===")

    # === Check if at least 1 argument is given ===

    try:
        if len(sys.argv) == 1:
            raise ValueError
    except ValueError:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return None

    # === Check if arguments are of type INT ===

    score_list = []

    try:
        score_list = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Error: All arguments must be valid integers")
        return None

    # === Score calculation ===

    i = 0
    score_range = max(score_list) - min(score_list)
    arg_count = len(score_list)

    print("Scores processed: [", end="")
    for score in score_list:
        if i == arg_count - 1:
            print(f"{score}]")
        else:
            print(f"{score}", end=", ")
        i += 1

    print(f"Total players: {arg_count}")

    print(f"Total score: {sum(score_list)}")

    average_score = sum(score_list) / arg_count
    print(f"Average score: {average_score}")

    print(f"Hight score: {max(score_list)}")

    print(f"Low score: {min(score_list)}")

    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
