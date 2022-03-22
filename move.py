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
    opposite_directions = {
        "NE": "SW",
        "E": "W",
        "SE": "NW",
        "SW": "NE",
        "W": "E",
        "NW": "SW"
    }
    direction_tuple_map = [
        {"NE": (-1, 0), "E": (0, 1), "SE": (1, 1), "SW": (1, 0), "W": (0, -1), "NW": (-1, -1)},
        {"NE": (-1, 0), "E": (0, 1), "SE": (1, 1), "SW": (1, 0), "W": (0, -1), "NW": (-1, -1)},
        {"NE": (-1, 0), "E": (0, 1), "SE": (1, 1), "SW": (1, 0), "W": (0, -1), "NW": (-1, -1)},
        {"NE": (-1, 0), "E": (0, 1), "SE": (1, 1), "SW": (1, 0), "W": (0, -1), "NW": (-1, -1)},
        {"NE": (-1, 0), "E": (0, 1), "SE": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, -1)},
        {"NE": (-1, 1), "E": (0, 1), "SE": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, 0)},
        {"NE": (-1, 1), "E": (0, 1), "SE": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, 0)},
        {"NE": (-1, 1), "E": (0, 1), "SE": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, 0)},
        {"NE": (-1, 1), "E": (0, 1), "SE": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, 0)}
    ]

    def __init__(self):
        self.direction_of_selected_pieces = None  # stores vector of selected game pieces

    def get_adj_game_spaces(self, row: int, col: int) -> set:
        """
        Gets all the game spaces adjacent to the selected game piece.
        :param row: an int, the number of the row
        :param col: an int, the number of the column
        :param num_pieces_selected: an int, the number of currently selected game pieces
        :return: a set, of the adjacent game spaces
        """
        adjacent_spaces = set()

        # if the row key is passed, then it is converted to the row number
        if type(row) != int:
            row = Converter.convert_row_to_string_or_int(row)

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

    def get_dir_of_selected_pieces(self, selected_pieces: list, num_pieces_selected: int) -> list:
        """
        Gets the vector of direction of the selected game pieces
        :param selected_pieces: a list, containing the external coordinates of the selected game piece(s)
        :param num_pieces_selected: an int, of the number of game pieces currently selected
        :return: a list, containing the direction of the selected game pieces
        """
        first_piece = selected_pieces[0]
        other_piece = selected_pieces[num_pieces_selected - 2]  # always indexes the 2nd last piece

        # gets the row num and column number of the 1st piece
        first_piece_row_num = Converter.convert_row_to_string_or_int(first_piece[0])
        first_piece_col_num = first_piece[1]

        # gets the row num and column number of the 2nd piece
        second_piece_row_num = Converter.convert_row_to_string_or_int(other_piece[0])
        second_piece_col_num = other_piece[1]

        # gets the difference of the row number and column number between the two pieces
        row_difference = first_piece_row_num - second_piece_row_num
        col_difference = first_piece_col_num - second_piece_col_num

        # gets the vector of direction from the direction tuple map by indexing the difference in row and column and
        # extracting the index, and getting the direction at that index
        selected_row_keys = list(self.direction_tuple_map[first_piece_row_num].keys())  # gets the dir keys for the specified row
        selected_row_values = list(self.direction_tuple_map[first_piece_row_num].values())  # gets the dir values for the specified row

        index = selected_row_values.index((row_difference, col_difference))  # gets the index of the difference in row and column
        direction_cardinal = selected_row_keys[index]  # gets the cardinal direction through indexing the row and col difference

        return [direction_cardinal, self.opposite_directions[direction_cardinal]]

    def get_adj_game_spaces_and_direction(self, row: int, col: int) -> set:
        """
        Gets all the game spaces adjacent to the selected game piece.
        :param row: an int, the number of the row
        :param col: an int, the number of the column
        :return: a set, of the adjacent game spaces
        """
        adjacent_spaces = set()

        # if the row key is passed, then it is converted to the row number
        if type(row) != int:
            row = Converter.convert_row_to_string_or_int(row)

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

    def get_possible_moves(self, num_pieces_selected: int, selected_pieces: list, game_board: dict, turn_color: str, vector_of_dir=None) -> set:
        """
        Gets the valid spaces for where the currently selected game piece(s) can move to. A tuple of 2 sets is returned.
        The first set contains the valid empty game spaces to make a move to, the second set contains adjacent spaces
        occupied by the opposing color
        :param num_pieces_selected: a int, the number of currently selected game pieces
        :param selected_pieces: a list, containing the external coordinates of the selected game pieces, in order
        :param game_board: the current game board
        :param: turn_color: the color of the current turn
        :param vector_of_dir: the vector of direction for when 2 or 3 pieces are selected
        :return: a tuple of sets, a tuple of 2 sets.
        """
        unoccupied_game_spaces = set()
        occupied_game_spaces = set()

        if num_pieces_selected == 1:

            # gets the current selected game piece and converts the notation from external to internal
            selected_piece = selected_pieces[0]

            # gets all adjacent spaces to the selected piece
            adjacent_spaces = self.get_adj_game_spaces_and_direction(selected_piece[0], selected_piece[1])

            # iterates over all adjacent spaces and filters out spaces that are occupied
            for space in adjacent_spaces:
                # converts external notation of current space on game board to internal notation
                space_internal_tuple = Converter.external_notation_to_internal(space)

                # extracts the row key and column number from the tuple
                row_key = space_internal_tuple[0]
                col_num = space_internal_tuple[1]

                try:
                    adjacent_space_color = game_board[row_key][col_num]["color"]

                    # means the adjacent space is unoccupied, if column number is < 0 then it is off the game board
                    if adjacent_space_color == None and col_num >= 0:
                        unoccupied_game_spaces.add(space)

                # means the adjacent space is off the game board
                except (IndexError, KeyError):
                    pass

        elif num_pieces_selected > 0:
            adjacent_spaces = set()

            # gets all adjacent spaces for all of the selected pieces
            for selected_piece in selected_pieces:
                selected_piece = Converter.external_notation_to_internal(selected_piece)

                adjacent_spaces.update(self.get_adj_game_spaces_and_direction(selected_piece[0], selected_piece[1]))

        return unoccupied_game_spaces
