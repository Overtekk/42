import sys


def ft_score_analytics() -> None:
    """
    Accepted arguments: a list of INT. It will be the player scores.
    Then, organize scores and make some calcules.
    """

    print("=== Player Score Analytics ===")

    # === Check if at least 1 argument is given ===

    if len(sys.argv) == 1:
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

    # === Show the score ===

    i = 0

    print("Scores processed: [", end="")
    for score in score_list:
        if i == score_list[-1]:
            print(f"{score}")
        else:
            print(f"{score}", end=",")
        i += 1
    print("]")


if __name__ == "__main__":
    ft_score_analytics()
