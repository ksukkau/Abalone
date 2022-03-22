from converter import Converter


class Move:
    """
    Encapsulates methods related to selected valid game pieces, moving selected game piece(s), or performing sumitos.
    """
    directions = [
        "NE",
        "E",
        "SE",
        "SW",
        "W",
        "NW"
    ]
    move_directions = {
        "NE": (-1, 1),
        "E": (0, 1),
        "SE": (1, 1),
        "SW": (1, -1),
        "W": (0, -1),
        "NW": (-1, -1)
    }

    def get_adj_game_spaces(self, row: int, col: int):
        """
        Gets all the game spaces adjacent to the selected game piece.
        :param row: an int, the number of the row
        :param col: an int, the number of the column
        :return: a set, of the adjacent game spaces
        """
        adjacent_spaces = set()

        # iterates through all possible directions around a given game piece
        for direction in self.directions:
            # gets the direction coordinate tuple, and gets the adjusted direction tuple
            direction_tuple = self.move_directions[direction]
            adjusted_direction_tuple = Converter.calculate_adjusted_direction_tuple(row, direction_tuple)

            # gets the internal notation of the adjacent piece
            adjacent_space_internal = Converter.simulate_game_piece_movement(row, col, adjusted_direction_tuple)
            # converts the internal notation to external notation
            adjacent_space_external = Converter.internal_notation_to_external(adjacent_space_internal[0], adjacent_space_internal[1])

            adjacent_spaces.add(adjacent_space_external)

        return adjacent_spaces
