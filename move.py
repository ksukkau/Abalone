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

    def __init__(self):
        self.direction_of_selected_pieces = None  # stores vector of selected game pieces

    def get_adj_game_spaces(self, row: int, col: int, num_pieces_selected=0, selected_pieces=None) -> set:
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

        if num_pieces_selected == 0:
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

        # gets the valid game pieces that can be selected
        elif num_pieces_selected > 1:
            self.get_dir_of_selected_pieces(selected_pieces)
            pass

        return adjacent_spaces

    def get_dir_of_selected_pieces(self, selected_pieces: list) -> tuple:
        """
        Gets the vector of selected game pieces
        :param selected_pieces: a list, containing the external coordinates of the selected game piece(s)
        :return: a list, containing the direction of the selected game pieces
        """
        vector_of_direction_tuple = self.get_direction_tuple_of_selected_pieces(selected_pieces[0], selected_pieces[1])
        vector_of_dir = []  # will contain the vector of selected pieces, as well is it's opposite direction

    def get_direction_tuple_of_selected_pieces(self, first_piece, second_piece) -> tuple:
        """
        Given two adjacent game pieces, the method turns the vector of direction that the pieces are selected on. Also
        adjusts the column based on which row the first piece is selected on (due to the hexagonal shaped game board)
        :param first_piece: a string, external notation of the 1st game piece selected
        :param second_piece: a string, external notation of the 2nd game piece selected
        :return: a tuple of ints, of the vector of direction of the selected game pieces
        """
        vertical_dir = 0
        horizontal_dir = 0

        first_piece_coords = Converter.external_notation_to_internal(first_piece)
        first_row_num = Converter.convert_row_to_string_or_int(first_piece_coords[0])
        first_col_num = first_piece_coords[1]

        second_piece_coords = Converter.external_notation_to_internal(second_piece)
        second_row_num = Converter.convert_row_to_string_or_int(second_piece_coords[0])
        second_col_num = second_piece_coords[1]

        # gets the row and column differences between the 2 selected pieces
        row_difference = first_row_num - second_row_num
        col_difference = first_col_num - second_col_num

        # checks if the 2nd piece is below or above the 1st, if not then it's along the same horizontal plane
        if row_difference < 0:  # means second piece is South of the 1st
            vertical_dir = 1
        elif row_difference > 0:  # means 2nd piece is North of the 1st
            vertical_dir = -1

        # checks for pieces in the top half of the board, including the middle row (row E/row 4)
        if first_row_num < 4:
            # adjusts for SW movement
            if vertical_dir == 1 and col_difference == 0:
                horizontal_dir = -1
            # adjusts for NE movement
            elif vertical_dir == -1 and col_difference == 0:
                horizontal_dir = 1

            # adjusts for SE movement
            elif vertical_dir == 1 and col_difference < 0:
                horizontal_dir = 1
            # adjusts for NW movement
            elif vertical_dir == -1 and col_difference > 0:
                horizontal_dir = -1

        # checks for pieces in the middle row (row E/row 4)
        elif first_row_num == 4:
            # adjusts for NE movement
            if vertical_dir == 1 and col_difference == 0:
                horizontal_dir = 1
            # adjusts for SE movement
            elif vertical_dir == -1 and col_difference == 0:
                horizontal_dir = 1

            # adjusts for SW movement
            elif vertical_dir == 1 and col_difference > 0:
                horizontal_dir = -1
            # adjusts for NW movement
            elif vertical_dir == -1 and col_difference > 0:
                horizontal_dir = -1

        # checks for pieces in the bottom half of the board, no including the middle row (row E/ row 4)
        elif first_row_num < 4:

            # adjusts for SE movement
            if vertical_dir == 1 and col_difference == 0:
                horizontal_dir = 1
            # adjusts for NW movement
            elif vertical_dir == -1 and col_difference == 0:
                horizontal_dir = -1

            # adjusts for SW movement
            elif vertical_dir == 1 and col_difference > 0:
                horizontal_dir = -1
            # adjusts for NE movement
            elif vertical_dir == -1 and col_difference < 0:
                horizontal_dir = 1

        # adjusts column direction for bottom half of the board
        if col_difference < 0 and row_difference != "":
            horizontal_dir = 1
        elif col_difference > 0 and row_difference == "":
            horizontal_dir = -1

        return vertical_dir, horizontal_dir

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

    def get_valid_moves(self, num_pieces_selected: int, selected_pieces: list, selected_pieces_xy_coords: list, game_board: dict, turn_color: str) -> tuple:
        """
        Gets the valid spaces for where the currently selected game piece(s) can move to. A tuple of 2 sets is returned.
        The first set contains the valid empty game spaces to make a move to, the second set contains adjacent spaces
        occupied by the opposing color
        :param num_pieces_selected: a int, the number of currently selected game pieces
        :param selected_pieces: a list, containing the external coordinates of the selected game pieces, in order
        :param selected_pieces_xy_coords: a list, containing the x & y coordinates of the selected game pieces, in order
        :param game_board: the current game board
        :param: turn_color: the color of the current turn
        :return: a tuple of sets, a tuple of 2 sets.
        """
        empty_game_spaces = set()
        occupied_game_spaces = set()

        if num_pieces_selected == 0:

            # gets the current selected game piece and converts the notation from external to internal
            selected_piece = selected_pieces[0]
            selected_piece_internal = Converter.external_notation_to_internal(selected_piece)

            # gets all adjacent spaces to the selected piece
            adjacent_spaces = self.get_adj_game_spaces_and_direction(selected_piece_internal[0], selected_piece_internal[1])

            for space in adjacent_spaces:
                # converts external notation of current space on game board to internal notation
                space_internal_tuple = Converter.external_notation_to_internal(space)

                # extracts the row key and column number from the tuple
                row_key = space_internal_tuple[0]
                col_num = space_internal_tuple[1]

                try:
                    adjacent_space = game_board[row_key][col_num]["color"]

                    # means the adjacent space is unoccupied
                    if adjacent_space == None:
                        empty_game_spaces.add(space)

                # means the adjacent space is off the game board
                except (IndexError, KeyError):
                    pass

        elif num_pieces_selected > 0:
            adjacent_spaces = set()

            # gets all adjacent spaces for all of the selected pieces
            for selected_piece in selected_pieces:
                selected_piece_internal = Converter.external_notation_to_internal(selected_piece)

                adjacent_spaces.update(self.get_adj_game_spaces_and_direction(selected_piece_internal[0], selected_piece_internal[1]))


        # # means the adjacent space is occupied by the opposing color
        # opposing_color = Converter.get_opposite_color(turn_color)
        # if adjacent_space == opposing_color:
        #     occupied_game_spaces.add(space)

        return empty_game_spaces, occupied_game_spaces
