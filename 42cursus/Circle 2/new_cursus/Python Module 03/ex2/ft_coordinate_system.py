import math


def input_coordinate(coord_str: str) -> tuple | None:
    """Build a 3D coordinate system using tuples.

    === Arguments ===
        - Coordinate in STRING format like ()"10, 20, 5")

    === Returns ===
        - Tuple: Player coordinate in tuple()
        - None: Nothing if input is incorrect

    This function take player coordinate send by the user and convert it to
    int. If it's not number, then we return None. Then, we put the coordinates
    in a tuple and calcule the distance between the origin (0, 0, 0) and the
    player position, then return the coords.
    """

    coord_pos_base = (0, 0, 0)
    x1, y1, z1 = coord_pos_base
    coord_player = ()

    try:
        coord_player = tuple(int(x) for x in coord_str.split(","))
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coord_str}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None

    print(f"Parsing coordinates: \"{coord_str}\"")

    x3, y3, z3 = coord_player
    coord_distance = math.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2)
    print(f"Parsed position: {coord_player}")
    print(f"Distance between {coord_pos_base} and {coord_player}: "
          f"{coord_distance}\n")

    return tuple(coord_player)


if __name__ == "__main__":
    """Here, we calcule a position we created and calcule the origin
    position (0, 0, 0) with it to know the distance. Then, we send player
    coordinate to the input_coordinate() function.
    """

    print("===Game Coordinate System===\n")

    coord_pos_base = (0, 0, 0)
    coord_pos = (10, 20, 5)

    x1, y1, z1 = coord_pos_base
    x2, y2, z2 = coord_pos

    coord_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(f"Position created: {coord_pos}")
    print(f"Distance between {coord_pos_base} and {coord_pos}: "
          f"{coord_distance:.2f}\n")

    coord_player = input_coordinate("3,4,0")
    input_coordinate("abc,def,ghi")  # Bad input to show error

    x3, y3, z3 = coord_player

    print("\nUnpacking demonstration:")
    print(f"Player at x={x3}, y={y3}, z={z3}")
    print(f"Coordinates: X={x3}, Y={y3}, Z={z3}")
