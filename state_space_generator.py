from game import *
from copy import deepcopy
import sys


class StateSpaceGenerator:
    """
    Encapsulates the methods required to generate the state space at any given game state.
    """

    def __init__(self):
        self.file_name = ''
        self.turn = ""
        self.board_text = ""
        self.possible_moves_single = set()
        self.possible_moves_double = set()
        self.possible_moves_triple = set()
        self.possible_moves_sumito = set()
        self.possible_moves_sumito_move_notation = set()
        self.possible_moves_sidestep = set()
        self.possible_moves_sidestep_move_notation = set()
        self.sumito_trailing_piece_turn_color = None
        self.sumito_leading_piece_opposing_color = None
        self.group = None
        self.game = GameBoard()
        self.reset_board = None
        self.rows = {
            "I": 0,
            "H": 1,
            "G": 2,
            "F": 3,
            "E": 4,
            "D": 5,
            "C": 6,
            "B": 7,
            "A": 8
        }
        self.colors = {
            "b": "black",
            "w": "white"
        }
        self.move_directions = {
            "NE": (-1, 1),
            "E": (0, 1),
            "SE": (1, 1),
            "SW": (1, -1),
            "W": (0, -1),
            "NW": (-1, -1)
        }
        self.opposite_direction = {
            "NE": "SW",
            "E": "W",
            "SE": "NW",
            "SW": "NE",
            "W": "E",
            "NW": "SE"
        }
        self.sidestep_directions = {
            "NE": ["E", "NW"],
            "E": ["NE", "NW"],
            "SE": ["E", "NE"],
            "SW": ["E", "NW"],
            "W": ["NE", "NW"],
            "NW": ["E", "NE"]
        }
        self.updated_game_board = None

    @staticmethod
    def convert_row_string_int(row_val):
        """
        If provided a string representing the game board dictionary row key, then the value is converted to an int of
        the row. If provided an int of the row of the game board, then the int is converted into a key for the game
        board dictionary.

        :precondition row_val: a string of a key from the game_board dictionary, or an int representing a row
        :param row_val: either a string or an integer
        :return: an int if passed a string, or a string if passed an int
        """
        if type(row_val) == str:
            row_num = int(row_val.replace("row", ''))
            return row_num
        elif type(row_val) == int:
            row_key = "row" + str(row_val)
            return row_key
        else:
            print("Invalid value passed. Argument must be a string or an integer.")

    @staticmethod
    def get_opposite_color(color):
        if color == "black":
            return "white"
        else:
            return "black"

    @staticmethod
    def calculate_column(row, col):
        """
        Calculates correct column number in game board array from given column number.

        :param row: row number: int
        :param col: column number as given: int
        :return:
        """
        rows = {
            0: 5,
            1: 4,
            2: 3,
            3: 2
        }

        if row in rows:
            col_coord = col - rows[row]
        else:
            col_coord = col - 1
        return col_coord

    def translate_single_piece_to_board_notation(self, piece: str) -> tuple:
        """
        Converts a piece from external board notation (e.g. H5) into the internal notation (e.g. '("row3, 4)).

        :param piece: string containing the piece location conforming to external board notation (e.g. 'B3')
        :return: a tuple (str, int) where the string is the row key and the int is  the column number
        """
        row = self.rows[piece[0]]
        row_key = "row" + str(row)

        col = int(piece[1])
        column = self.calculate_column(row, col)
        return row_key, column

    def translate_test_input_to_board_notation(self):
        """
        Creates a game board array based on test input.

        :return: None
        """
        self.game.initialize_game_board_array()

        piece_list = self.board_text.split(',')
        for item in piece_list:
            row = self.rows[item[0]]
            row_key = "row" + str(row)
            col = int(item[1])
            color = self.colors[item[2]]
            column = self.calculate_column(row, col)
            row_list = self.game.game_board[row_key]
            row_list[column]['color'] = color

    def get_current_board(self):
        """
        Gets current board from game.
        """
        current_board = self.game.game_board
        # for reading from our actual board not applicable for test input im not sure we even need this...

    def get_player_turn(self):
        """
        Gets current turn from game
        """
        self.turn = self.game.turn
        # for reading from our actual board not applicable for test input

    def get_piece_coords_movement(self, row_num, col_num: int, direction: tuple) -> tuple:
        """
        Gets the coordinates of the provided piece if it were to move in the provided direction.

        :param row_num: a string of the row key, or an int of the row number
        :param col_num: an int of the column number
        :param direction: a tuple containing the direction of movement
        :return: a tuple (str, int) where the string is the row key and the int is  the column number
        """
        row_dir = direction[0]
        col_dir = self.calc_new_direction_coords(row_num, direction)

        if type(row_num) != int:
            row_num = self.convert_row_string_int(row_num)

        new_row_num = row_num + row_dir
        new_col_num = col_num + col_dir

        new_row_key = self.convert_row_string_int(new_row_num)
        return new_row_key, new_col_num

    def create_piece_list_for_current_turn(self):
        """
        Iterates through the game board and calls helper methods to all possible moves given a specific board state.
        """
        # create an image of board before changes
        self.updated_game_board = deepcopy(self.game.game_board)

        for row_key in self.game.game_board:
            row = self.game.game_board[row_key]
            for column_detail in row:
                # if "white" in column_detail.values():
                #     print(column_detail)
                if self.turn in column_detail.values():
                    self.generate_inline_moves(row_key, column_detail)
                    self.generate_sidestep_moves(row_key, column_detail)

    def get_leading_or_trailing_piece(self, row_num, col_num: int, num_of_adj_pieces: int, direction: tuple) -> tuple:
        """
        Gets the first (leading) or last (trailing) piece when provided the location of a specific piece along with the
        number of pieces adjacent to it, and the direction of the vector of the adjacent pieces.

        :param row_num: a string of the row key, or an int of the row number
        :param col_num: an int of the column number
        :param num_of_adj_pieces: an int, the number of pieces adjacent to the provided piece
        :param direction: a tuple containing the direction of movement
        :return: a tuple (str, int) where the string is the row key and the int is  the column number
        """
        if num_of_adj_pieces > 0:

            if type(row_num) != int:
                row_num = self.convert_row_string_int(row_num)

            row_dir = direction[0]
            col_dir = self.calc_new_direction_coords(row_num, direction)
            for pieces in range(0, num_of_adj_pieces):
                row_num = row_num + row_dir
                col_num = col_num + col_dir

                col_dir = self.calc_new_direction_coords(row_num, direction)

            row_key = self.convert_row_string_int(row_num)
            return row_key, col_num

        else:
            row_key = self.convert_row_string_int(row_num)
            return row_key, col_num

    def get_sumito_num_of_adj_pieces(self, piece_color: str, row_key: str, col_num: int, direction: str, groupings=2) -> int:
        """
        Gets the number of adjacent pieces of the same color passed to this method. Checks the pieces adjacent to the
        specified piece in the specified vector of direction. The number of groups can be specified to determine if the
        method searches for 2 or 3 piece groupings.

        :param piece_color: a string, the color of the adjacent pieces to get
        :param row_key: a string, containing the row of the piece to find adjacent pieces for
        :param col_num: an int, containing the column of the piece to find adjacent pieces for
        :param direction: a string of the raw cardinal direction of movement (e.g. 'NE' or 'S')
        :param groupings: an int, the number of grouped pieces to perform a sumito, set to 2 by default
        :return: an int, the number of pieces adjacent to the groupings
        """
        row_num = self.convert_row_string_int(row_key)
        opposite_dir_coords = self.move_directions[self.opposite_direction[direction]]
        processed_opposite_dir = (opposite_dir_coords[0], self.calc_new_direction_coords(row_num, opposite_dir_coords))

        new_row_num = processed_opposite_dir[0] + row_num
        new_row_key = self.convert_row_string_int(new_row_num)
        new_col_num = processed_opposite_dir[1] + col_num

        num_of_adj_pieces = 0
        adj_space_piece_color = self.updated_game_board[new_row_key][new_col_num]["color"]
        try:
            # checks if adjacent, 2nd, piece is same color
            if adj_space_piece_color == piece_color:
                num_of_adj_pieces += 1

            new_col_num = self.calc_new_direction_coords(new_row_num, opposite_dir_coords) + new_col_num
            new_row_num = processed_opposite_dir[0] + new_row_num

            if new_row_num < 0:
                return num_of_adj_pieces
            new_row_key = self.convert_row_string_int(new_row_num)

            adj_space_piece_color = self.updated_game_board[new_row_key][new_col_num]["color"]
            # checks if adjacent, 3rd, piece is same color
            if (adj_space_piece_color == piece_color) and groupings == 3:
                num_of_adj_pieces += 1

        except IndexError:
            # print("Adjacent piece check out of board area")
            return num_of_adj_pieces

        return num_of_adj_pieces

    def translate_piece_value_for_output(self, row_num, col_num: int) -> str:
        """
        Translates piece from internal coordinates to notation as required by game board coordinate system.

        :param row_num: a string of the row key, or an int of the row number
        :param col_num: an int of the column number
        :return: a string of the specified piece conforming to external board notation (e.g. H5)
        """
        ASCII_ALPHABET_OFFSET = 8
        ZERO_INDEX_OFFSET = 1

        TOP_ROW = 0
        UPPER_HALF = range(1, 4 + ZERO_INDEX_OFFSET)

        # if the string row_key is passed, then it is converted to an int representing the row
        if type(row_num) != int:
            row_num = self.convert_row_string_int(row_num)

        num_of_cols = self.game.calculate_row_length(row_num)

        if row_num == TOP_ROW:
            col_coord = num_of_cols + col_num
        elif row_num in UPPER_HALF:
            col_coord = (num_of_cols - (row_num * 2)) + col_num
        else:
            col_coord = col_num + ZERO_INDEX_OFFSET

        row_coord = chr((ASCII_ALPHABET_OFFSET - row_num) + 65)
        return row_coord + str(col_coord)

    def generate_inline_moves(self, row_key: str, column_detail: dict):
        """
        Runs the engine to find all of the possible inline moves for 2 and 3 groupings, as well as 2 and 3 grouped
        sumitos.

        :param row_key: a string containing the row (e.g. 'row4')
        :param column_detail: a dictionary containing the pieces for a row
        """
        row_num = self.convert_row_string_int(row_key)
        col_num = column_detail['colNum']
        piece = self.translate_piece_value_for_output(row_num, col_num)

        for direction in self.move_directions:
            direction_tuple = self.move_directions.get(direction)

            new_row_num = self.convert_row_string_int(row_key) + direction_tuple[0]
            new_col_num = col_num + self.calc_new_direction_coords(row_num, direction_tuple)
            new_row_key = self.convert_row_string_int(new_row_num)

            try:
                space_value = self.game.game_board[new_row_key][new_col_num]['color']
                if space_value is None:
                    # piece can move
                    pieces = (piece, piece)
                    # generate single piece inline move

                    # gets moves for a single piece
                    self.possible_moves_single.add(("i", pieces, direction, new_row_key, new_col_num))

                    # gets moves for multiple pieces grouped
                    self.possible_multiple_piece_inline_groups(direction, row_key, col_num, new_row_num, new_col_num)

                # checks for valid sumito
                opposite_color = self.get_opposite_color(self.turn)
                if space_value == opposite_color:

                    sumito_groupings = 2
                    while sumito_groupings < 4:
                        num_of_adj_selected_pieces = self.get_sumito_num_of_adj_pieces(self.turn, row_key, col_num,
                                                                                       direction, sumito_groupings)

                        opposite_direction = self.opposite_direction[direction]
                        opposite_direction_tuple = self.move_directions[opposite_direction]
                        num_of_adj_opposing_pieces = self.get_sumito_num_of_adj_pieces("white", new_row_key,
                                                                                       new_col_num, opposite_direction,
                                                                                       sumito_groupings)

                        # if num of adjacent pieces of current color is greater than num of adjacent pieces of opposing
                        # color them sumito is performed
                        if num_of_adj_selected_pieces > num_of_adj_opposing_pieces:
                            # getting row and col of space where sumito'ed piece is going to end up

                            leading_piece = self.get_leading_or_trailing_piece(new_row_num, new_col_num,
                                                                               num_of_adj_opposing_pieces,
                                                                               direction_tuple)
                            piece_in_front_leading_piece = self.get_leading_or_trailing_piece(leading_piece[0],
                                                                                              leading_piece[1], 1,
                                                                                              direction_tuple)

                            piece_in_front_row = piece_in_front_leading_piece[0]
                            piece_in_front_col = piece_in_front_leading_piece[1]
                            try:
                                # checks if the space in front of the leading space is un-occupied
                                if self.updated_game_board[piece_in_front_row][piece_in_front_col]["color"] is None:
                                    self.add_valid_sumito_to_move_set(col_num, direction,
                                                                                      direction_tuple, leading_piece,
                                                                                      num_of_adj_selected_pieces,
                                                                                      opposite_direction_tuple, piece,
                                                                                      row_num)

                            # if an IndexError is raised, that means a piece is going to be pushed off the board
                            except IndexError:
                                self.add_valid_sumito_to_move_set(col_num, direction,
                                                                  direction_tuple, leading_piece,
                                                                  num_of_adj_selected_pieces,
                                                                  opposite_direction_tuple, piece,
                                                                  row_num)

                        sumito_groupings += 1

            except IndexError:
                # print("Sumito check outside board area")
                pass

    def possible_multiple_piece_inline_groups(self, direction: str, row_key: str, col_num: int, new_row: int, new_column: int):
        """
        Finds the possible valid moves for inline moves with 2 and 3 piece groupings.

        :param direction: a string of the raw cardinal direction of movement (e.g. 'NE' or 'S')
        :param row_key: a string of the row key
        :param col_num: an int of the column number
        :param new_row: an int of the row of the desired space to move to
        :param new_column: an int of the new column of desired space to move to
        """
        selected_row_num = self.convert_row_string_int(row_key)

        opposite_dir = self.opposite_direction.get(direction)
        opposite_dir_coords = self.move_directions[opposite_dir]

        adj_new_row_num = selected_row_num + opposite_dir_coords[0]
        ajd_piece_row_key = self.convert_row_string_int(adj_new_row_num)
        adj_piece_col_num = col_num + self.calc_new_direction_coords(selected_row_num, opposite_dir_coords)

        if self.is_valid_adjacent_piece(ajd_piece_row_key, adj_piece_col_num):
            leading_piece_coords = self.translate_piece_value_for_output(selected_row_num, col_num)
            trailing_piece_coords = self.translate_piece_value_for_output(adj_new_row_num, adj_piece_col_num)

            pieces = (leading_piece_coords, trailing_piece_coords)
            new_row_key = self.convert_row_string_int(new_row)

            self.possible_moves_double.add(("i", pieces, direction, new_row_key, new_column))

            # Checks for 3-piece move group
            # ----------------------------------------------------------------------------------------------------
            adj_new_row_num = adj_new_row_num + opposite_dir_coords[0]
            adj_piece_row_key = self.convert_row_string_int(adj_new_row_num)
            adj_piece_col_num = adj_piece_col_num + self.calc_new_direction_coords(selected_row_num,
                                                                                   opposite_dir_coords)

            if self.is_valid_adjacent_piece(adj_piece_row_key, adj_piece_col_num):
                leading_piece_coords = self.translate_piece_value_for_output(selected_row_num, col_num)
                trailing_piece_coords = self.translate_piece_value_for_output(adj_new_row_num, adj_piece_col_num)

                pieces = (leading_piece_coords, trailing_piece_coords)
                new_row_key = self.convert_row_string_int(new_row)

                self.possible_moves_triple.add(("i", pieces, direction, new_row_key, new_column))

    def add_valid_sumito_to_move_set(self, col_num: int, direction: str, direction_tuple: tuple, leading_piece: tuple, num_of_adj_selected_pieces: int, opposite_direction_tuple: tuple, piece: str, row_num: int):
        """
        Helper method containing the logic to perform the sumito. Adds the type of move, the pieces involved in the
        sumito, the direction of movement, as well as the internal board coordinates of game board space the movement
        is going to occur. Also generates the move notation for sumitos.

        :param col_num: a int, of the column number of the selected piece
        :param direction: a string of the raw cardinal direction (e.g. 'NE', 'W')
        :param direction_tuple: a tuple containing the coordinates of the direction of movement (e.g. '(-1, 1)')
        :param leading_piece: a tuple containing the internal coordinates of the leading piece
        :param num_of_adj_selected_pieces: an int of the number of pieces adjacent to the selected piece
        :param opposite_direction_tuple: a tuple containing the coordinates of the opposite direction of movement
        :param piece: a str of the selected piece in external board notatation (e.g. 'G3')
        :param row_num: an int
        :return:
        """
        leading_piece_color = self.updated_game_board[leading_piece[0]][leading_piece[1]]["color"]
        if leading_piece_color != self.turn:
            trailing_piece = self.get_leading_or_trailing_piece(row_num, col_num, num_of_adj_selected_pieces,
                                                                opposite_direction_tuple)

            leading_piece_row_num = self.convert_row_string_int(leading_piece[0])
            leading_piece_col_num = leading_piece[1]
            empty_space_coords = self.get_piece_coords_movement(leading_piece_row_num, leading_piece_col_num,
                                                                direction_tuple)

            leading_piece = self.translate_piece_value_for_output(leading_piece[0], leading_piece[1])
            second_place_piece = self.get_piece_coords_movement(leading_piece_row_num, leading_piece_col_num,
                                                                opposite_direction_tuple)
            second_place_piece = self.translate_piece_value_for_output(second_place_piece[0], second_place_piece[1])
            trailing_piece = self.translate_piece_value_for_output(trailing_piece[0], trailing_piece[1])
            pieces = (leading_piece, second_place_piece, trailing_piece)
            self.possible_moves_sumito.add(("i", pieces, direction, empty_space_coords[0], empty_space_coords[1]))

            move_notation_pieces = (piece, trailing_piece)
            self.possible_moves_sumito_move_notation.add(
                ("i", move_notation_pieces, direction, empty_space_coords[0], empty_space_coords[1]))

    def is_valid_adjacent_piece(self, opposite_adj_row_key: str, opposite_adj_col_num: int) -> bool:
        """
        Checks if the piece behind is of the same color, and returns a true if it is, or else false is returned.

        :param opposite_adj_col_num: a string of row_key of the adjacent piece to be checked
        :param opposite_adj_row_key: an int, of the column of the adjacent piece to be checked
        :return: a boolean
        """

        # checks if the adjacent piece in the opposing direction of movement is the same color as the select piece
        try:
            if self.updated_game_board[opposite_adj_row_key][opposite_adj_col_num]["color"] == self.turn:
                return True
            else:
                return False

        except IndexError:
            # print("Adjacent 2nd piece out of board area")
            return False

    def generate_sidestep_moves(self, row_key: str, column_detail: dict):
        """
        Generates and finds all legal sidestep moves for a given board state.

        :param row_key: a string containing the row (e.g. 'row4')
        :param column_detail: a dictionary containing the pieces for a row
        """
        row_num = self.convert_row_string_int(row_key)
        col_num = column_detail['colNum']
        piece = self.translate_piece_value_for_output(row_num, col_num)

        for direction in self.move_directions:
            direction_tuple = self.move_directions.get(direction)

            new_row_num = self.convert_row_string_int(row_key) + direction_tuple[0]
            new_col_num = col_num + self.calc_new_direction_coords(row_num, direction_tuple)
            new_row_key = self.convert_row_string_int(new_row_num)

            try:
                space_value = self.game.game_board[new_row_key][new_col_num]['color']
                if space_value is None:

                    # sets the grouping of sidesteps to find possible moves for
                    sidestep_groupings = 2
                    while sidestep_groupings < 4:

                        # gets the complimentary sidesteps directions to check for
                        sidestep_dirs_to_check = self.sidestep_directions[direction]
                        for sidestep_complimentary_dir in sidestep_dirs_to_check:
                            num_of_adj_pieces = self.get_sidestep_num_of_adj_pieces(self.turn, row_key, col_num,
                                                                                    sidestep_complimentary_dir,
                                                                                    sidestep_groupings)

                            if num_of_adj_pieces > 0:
                                # gets the sidestep move direction coords
                                sidestep_complimentary_dir_tuple = self.move_directions[sidestep_complimentary_dir]

                                adj_piece_row = row_num
                                adj_piece_col = col_num
                                adj_piece_coords = self.get_piece_coords_movement(adj_piece_row, adj_piece_col,
                                                                                  sidestep_complimentary_dir_tuple)

                                # checks all of the adjacent pieces to see if they are able to perform a sidestep
                                for adj_piece in range(0, num_of_adj_pieces):
                                    # gets the coords of the adjacent piece
                                    adj_piece_coords = self.get_piece_coords_movement(adj_piece_row, adj_piece_col,
                                                                                      sidestep_complimentary_dir_tuple)

                                    adj_piece_row = adj_piece_coords[0]
                                    adj_piece_col = adj_piece_coords[1]

                                # gets trailing piece and con
                                # verts it to external board notation (e.g. H6)
                                trailing_piece = self.translate_piece_value_for_output(adj_piece_coords[0],
                                                                                       adj_piece_coords[1])

                                # checks if the adjacent piece can make a sidestep
                                sidestep_space = self.get_piece_coords_movement(adj_piece_row, adj_piece_col,
                                                                                direction_tuple)

                                # checks if the space that the adjacent piece wants to sidestep to is empty
                                try:
                                    if self.updated_game_board[sidestep_space[0]][sidestep_space[1]]["color"] is None:

                                        # handles adding 3 group side steps to the move list
                                        if num_of_adj_pieces == 2:
                                            # gets middle piece and converts it to external board notation (e.g. H6)
                                            middle_piece_tuple = self.get_piece_coords_movement(row_num, col_num,
                                                                                                sidestep_complimentary_dir_tuple)
                                            middle_piece = self.translate_piece_value_for_output(middle_piece_tuple[0],
                                                                                                 middle_piece_tuple[1])

                                            # add pieces to a tuple and adds the move into the sidestep moves set
                                            pieces = (piece, middle_piece, trailing_piece)
                                            self.possible_moves_sidestep.add(
                                                ("s", pieces, direction, new_row_key, new_col_num))

                                            # adds pieces to the move notation set
                                            pieces_move_notation = (piece, trailing_piece)
                                            self.possible_moves_sidestep_move_notation.add(
                                                ("s", pieces_move_notation, direction, new_row_key, new_col_num))

                                        # handles adding 2 group side steps to the move list
                                        elif num_of_adj_pieces == 1:
                                            adj_piece_board_notation = self.translate_piece_value_for_output(adj_piece_row, adj_piece_col)
                                            pieces = (piece, adj_piece_board_notation)
                                            self.possible_moves_sidestep.add(("s", pieces, direction, new_row_key, new_col_num))

                                            # adds the pieces to the move notation set
                                            pieces_move_notation = (piece, adj_piece_board_notation)
                                            self.possible_moves_sidestep_move_notation.add(("s", pieces_move_notation, direction, new_row_key, new_col_num))

                                except IndexError:
                                    # print("Sidestep check out of board area")
                                    pass

                        sidestep_groupings += 1

            except IndexError:
                # print("outside board area")
                pass

    def possible_multiple_piece_sidestep_groups(self, direction: str, row_key: str, col_num: int, new_row: int, new_column: int):
        """
        Finds all the legal sidestep moves for 2 and 3 piece groupings.

        :param direction: a string, the raw cardinal direction of movement (e.g. 'NW' or 'E')
        :param row_key: a string, the row key
        :param col_num: an int, the column number
        :param new_row: an int, the number of the row adjacent to the selected piece to be checked
        :param new_column: an int, the number of the column adjacent to the selected piece to be checked
        """
        selected_row_num = self.convert_row_string_int(row_key)

        opposite_dir = self.opposite_direction.get(direction)
        opposite_dir_coords = self.move_directions[opposite_dir]

        adj_new_row_num = selected_row_num + opposite_dir_coords[0]
        ajd_piece_row_key = self.convert_row_string_int(adj_new_row_num)
        adj_piece_col_num = col_num + self.calc_new_direction_coords(selected_row_num, opposite_dir_coords)

        if self.is_valid_adjacent_piece(ajd_piece_row_key, adj_piece_col_num):
            leading_piece_coords = self.translate_piece_value_for_output(selected_row_num, col_num)
            trailing_piece_coords = self.translate_piece_value_for_output(adj_new_row_num, adj_piece_col_num)

            pieces = (leading_piece_coords, trailing_piece_coords)
            new_row_key = self.convert_row_string_int(new_row)

            self.possible_moves_double.add(("i", pieces, direction, new_row_key, new_column))

            # Checks for 3-piece move group
            # ----------------------------------------------------------------------------------------------------
            adj_new_row_num = adj_new_row_num + opposite_dir_coords[0]
            adj_piece_row_key = self.convert_row_string_int(adj_new_row_num)
            adj_piece_col_num = adj_piece_col_num + self.calc_new_direction_coords(selected_row_num,
                                                                                   opposite_dir_coords)

            if self.is_valid_adjacent_piece(adj_piece_row_key, adj_piece_col_num):
                leading_piece_coords = self.translate_piece_value_for_output(selected_row_num, col_num)
                trailing_piece_coords = self.translate_piece_value_for_output(adj_new_row_num, adj_piece_col_num)

                pieces = (leading_piece_coords, trailing_piece_coords)
                new_row_key = self.convert_row_string_int(new_row)

                self.possible_moves_triple.add(("i", pieces, direction, new_row_key, new_column))

    def get_sidestep_num_of_adj_pieces(self, piece_color: str, row_key: str, col_num: int, direction: str, groupings=2):
        """
        Finds the number of adjacent pieces that can make a legal sidestep move.

        :param piece_color: a string, the color of the adjacent pieces to get
        :param row_key: a string, containing the row key (e.g. 'row3')
        :param col_num: an int, containing the column number
        :param direction: a string of the raw caridnal direction (e.g. 'NE' or 'W')
        :param groupings: an int, the number of grouped pieces to search for, set to 2 by default
        :return: an int, the number of pieces adjacent to the specified piece
        """
        row_num = self.convert_row_string_int(row_key)
        dir_coords = self.move_directions[direction]
        processed_dir_coords = (dir_coords[0], self.calc_new_direction_coords(row_num, dir_coords))

        new_row_num = processed_dir_coords[0] + row_num
        new_row_key = self.convert_row_string_int(new_row_num)
        new_col_num = processed_dir_coords[1] + col_num

        num_of_adj_pieces = 0
        adj_space_piece_color = self.updated_game_board[new_row_key][new_col_num]["color"]
        try:
            # checks if adjacent, 2nd, piece is same color
            if adj_space_piece_color == piece_color:
                num_of_adj_pieces += 1
            else:
                return num_of_adj_pieces

            new_col_num = self.calc_new_direction_coords(new_row_num, dir_coords) + new_col_num
            new_row_num = processed_dir_coords[0] + new_row_num

            if new_row_num < 0:
                return num_of_adj_pieces
            new_row_key = self.convert_row_string_int(new_row_num)

            adj_space_piece_color = self.updated_game_board[new_row_key][new_col_num]["color"]
            # checks if adjacent, 3rd, piece is same color
            if (adj_space_piece_color == piece_color) and groupings == 3:
                num_of_adj_pieces += 1

        except IndexError:
            # print("Adjacent piece check out of board area")
            return num_of_adj_pieces

        return num_of_adj_pieces

    def update_board(self):
        """
        Contains for-loops to iterate over the sets of different types of moves, updates the board state for each move,
        and writes the board state to a .board file.
        """
        for move in self.possible_moves_single:
            # only for single piece moves
            if move[0] == 'i':
                # move front piece up
                self.updated_game_board[move[3]][move[4]]['color'] = self.turn
                # remove back piece
                location = self.translate_single_piece_to_board_notation(move[1][1])
                self.updated_game_board[location[0]][location[1]]['color'] = None
                self.output_board()
                # resets board to before move
                self.updated_game_board = deepcopy(self.game.game_board)

        for move in self.possible_moves_double:
            # only for single piece moves
            if move[0] == 'i':
                # move trailing piece up front
                self.updated_game_board[move[3]][move[4]]["color"] = self.turn

                trailing_piece_external_coords = move[1][1]
                trailing_piece_coords = self.translate_external_coords_to_internal_coords(
                    trailing_piece_external_coords)
                # remove old trailing piece
                self.updated_game_board[trailing_piece_coords[0]][trailing_piece_coords[1]]["color"] = None
                self.output_board()
                # resets board to before move
                self.updated_game_board = deepcopy(self.game.game_board)

        for move in self.possible_moves_triple:
            # only for single piece moves
            if move[0] == 'i':
                # move trailing piece up front
                self.updated_game_board[move[3]][move[4]]["color"] = self.turn

                trailing_piece_external_coords = move[1][1]
                trailing_piece_coords = self.translate_external_coords_to_internal_coords(
                    trailing_piece_external_coords)
                # remove old trailing piece
                self.updated_game_board[trailing_piece_coords[0]][trailing_piece_coords[1]]["color"] = None
                self.output_board()
                # resets board to before move
                self.updated_game_board = deepcopy(self.game.game_board)

        for move in self.possible_moves_sumito:
            # only for single piece moves
            if move[0] == 'i':

                leading_piece_coords = self.translate_single_piece_to_board_notation(move[1][0])
                second_place_piece_coords = self.translate_single_piece_to_board_notation(move[1][1])
                trailing_piece_coords = self.translate_single_piece_to_board_notation(move[1][2])

                opposing_color = self.get_opposite_color(self.turn)
                color_of_second_piece = \
                self.updated_game_board[second_place_piece_coords[0]][second_place_piece_coords[1]]["color"]

                try:
                    # push opposing piece
                    self.updated_game_board[move[3]][move[4]]["color"] = opposing_color

                except IndexError:
                    # shift pieces as piece has been pushed off game board
                    sumitoed_piece = self.translate_piece_value_for_output(leading_piece_coords[0], leading_piece_coords[1])

                    print(f"{sumitoed_piece + opposing_color[0]} pushed off the board!")

                finally:
                    # leading piece replaced by color of piece directly behind it
                    self.updated_game_board[leading_piece_coords[0]][leading_piece_coords[1]][
                        "color"] = color_of_second_piece

                    # replaces second place piece with piece of turn color
                    self.updated_game_board[second_place_piece_coords[0]][second_place_piece_coords[1]][
                        "color"] = self.turn

                    # removes trailing piece
                    self.updated_game_board[trailing_piece_coords[0]][trailing_piece_coords[1]]["color"] = None

                self.output_board()
                # resets board to before move
                self.updated_game_board = deepcopy(self.game.game_board)

        for move in self.possible_moves_sidestep:

            piece_sidestep_list = move[1]
            direction = move[2]
            direction_tuple = self.move_directions[direction]
            for piece in piece_sidestep_list:
                piece_coords_tuple = self.translate_external_coords_to_internal_coords(piece)

                # removes where the piece used to be
                self.updated_game_board[piece_coords_tuple[0]][piece_coords_tuple[1]]["color"] = None

                # gets the direction of the side step and packs the direction into a tuple
                sidestep_row_dir_coord = direction_tuple[0]
                sidestep_col_dir_coord = self.calc_new_direction_coords(piece_coords_tuple[0], direction_tuple)
                sidestep_dir_tuple = (sidestep_row_dir_coord, sidestep_col_dir_coord)

                # performs the sidestep
                sidestep_piece = self.get_piece_coords_movement(piece_coords_tuple[0], piece_coords_tuple[1],
                                                                sidestep_dir_tuple)
                self.updated_game_board[sidestep_piece[0]][sidestep_piece[1]]["color"] = self.turn

            self.output_board()
            # resets board to before move
            self.updated_game_board = deepcopy(self.game.game_board)

    def translate_external_coords_to_internal_coords(self, piece_coord: str) -> tuple:
        """
        Provided piece notation in the format of external coordinates (e.g. 'H4'), it converts the coordinates to
        internal board coordinates.

        :param piece_coord: a string, external board coordinates used to represent a piece (e.g. 'H5')
        :return: a tuple, (str, int), where the string is the row key, e.g. "row3", and the int is the column number
        """
        ASCII_OFFSET = 65
        NUM_OF_ROWS_OFFSET = 8

        row_letter = piece_coord[0]

        row_num = (ord(row_letter) - ASCII_OFFSET - NUM_OF_ROWS_OFFSET) * -1
        col_num = self.calculate_column(row_num, int(piece_coord[1]))

        if row_num < 0:
            print("Out of range coordinates passed to transate_external_coords_to_internal_coords")

        row_key = self.convert_row_string_int(row_num)
        return row_key, col_num

    def calc_new_direction_coords(self, row_num, direction):
        """
        Calculate the coordinates of the new direction given the current row and column of the game piece, as well as
        the direction of movement. Required due to the varying columns on each row on the game board because of the
        hexagonal shaped game board.

        :param row_num: an int, representing the row of the selected game piece
        :param direction: a tuple, containing the new movement as (x,y) or (row, col)
        :return: a int, containing the direction of the new movement along the column (west to east vector)
        """
        ZERO_INDEX_OFFSET = 1
        UPPER_HALF = range(1, 4 + ZERO_INDEX_OFFSET)
        MIDDLE_ROW = 4

        new_row_dir = direction[0]
        new_col_dir = direction[1]

        # if the string row_key is passed, then it is converted to an int representing the row
        if type(row_num) != int:
            row_num = self.convert_row_string_int(row_num)

        if row_num in UPPER_HALF:
            # checks for SE movement for pieces in the middle row
            if row_num == MIDDLE_ROW and new_row_dir == 1:
                if new_col_dir == 1:
                    new_col_dir = 0

            if row_num == MIDDLE_ROW and new_row_dir == -1:
                if new_col_dir == 1:
                    new_col_dir = 0

            # checks for NE movement
            elif new_row_dir == -1 and row_num != MIDDLE_ROW:
                if new_col_dir == 1:
                    new_col_dir = 0

            # checks for SW movement
            elif new_row_dir == 1 and row_num != MIDDLE_ROW:
                if new_col_dir == -1:
                    new_col_dir = 0

        # checks for pieces in the bottom half of the game board
        else:
            # checks for NW movement
            if new_row_dir == -1:
                if new_col_dir == -1:
                    new_col_dir = 0

            # checks for SE movement
            elif new_row_dir == 1:
                if new_col_dir == 1:
                    new_col_dir = 0

        return new_col_dir

    def read_test_input(self):
        """
        Reads test input and sets the board and turn.
        """
        colors = {
            "b": "black",
            "w": "white"
        }
        with open(f"{self.file_name}.input", 'r') as input_file:
            self.turn = colors[input_file.readline().replace('\n', '')]
            self.board_text = input_file.readline()


    def output_board(self):
        """
        Given the current board state, it generates a list containing the positions of the black and white game pieces
        and calls a helper method to write these lists to a text file.
        """
        blacks = []
        whites = []

        for row, col in self.updated_game_board.items():
            for piece in col:

                if piece["color"] is not None:

                    row_num = self.convert_row_string_int(row)
                    col_num = piece["colNum"]
                    piece_letter_coord = self.translate_piece_value_for_output(row_num, col_num)

                    if piece["color"] == "black":
                        blacks.append(piece_letter_coord + 'b')
                    else:
                        whites.append(piece_letter_coord + 'w')

        self.print_to_text_file(sorted(blacks) + sorted(whites))

    def text_output_moves(self):
        """
        Outputs move in move notation conforming to the move notation provided.
        """
        possible_moves = set().union(self.possible_moves_single).union(self.possible_moves_double) \
            .union(self.possible_moves_triple).union(self.possible_moves_sumito_move_notation).union(self.possible_moves_sidestep_move_notation)
        with open(f"{self.file_name}.moves", "a") as file:
            for i in possible_moves:
                move_type = i[0]
                pieces = i[1]
                direction = i[2]
                item = f"{move_type}-{pieces[0]}-{pieces[1]}-{direction}"
                file.write(item)
                file.write("\n")

    def print_to_text_file(self, item: list):
        """
        Writes the list containing the black and white game pieces for any given board game state to a text file with
        a .board file extension.

        :param item: a list, containing the black and white pieces on any given board game state
        :return:
        """
        item = str(item)
        item = item.replace('[', '').replace(']', '').replace(' ', '').replace("'", '')
        with open(f"{self.file_name}.board", "a") as file:
            file.write(item)
            file.write("\n")

    def run_tests(self):
        """
        Main method to call helper methods to run the state space generator.
        """
        self.read_test_input()
        self.translate_test_input_to_board_notation()
        self.create_piece_list_for_current_turn()
        self.update_board()
        self.text_output_moves()


def main():
    """
    Main function for the statespace generator tests.
    """
    s = StateSpaceGenerator()
    s.file_name = sys.argv[1].split('.')[0]
    s.run_tests()


if __name__ == '__main__':
    main()
