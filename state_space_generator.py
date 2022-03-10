import math
from settings import *
from tkinter import *
import tkinter as tk
from game import *
from copy import deepcopy


class StateSpaceGenerator:
    """
    Encapsulates the methods required to generate the state space at any given game state.
    """

    def __init__(self):
        self.turn = ""
        self.board_text = ""
        self.possible_moves_single = set()
        self.possible_moves_double = set()
        self.possible_moves_triple = set()
        self.possible_moves_sumito = set()
        self.sumito_trailing_piece = None
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
        self.updated_game_board = None

    def read_test_input(self, path):
        """
        Reads test input and sets the board and turn
        :param path: filepath to test input
        :return: None
        """
        colors = {
            "b": "black",
            "w": "white"
        }
        with open(path, 'r') as input_file:
            self.turn = colors[input_file.readline().replace('\n', '')]
            self.board_text = input_file.readline()

    def translate_single_piece_to_board_notation(self, piece):

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

    def get_current_board(self):
        """
        Gets current board from game.
        :return:
        """
        current_board = self.game.game_board
        # for reading from our actual board not applicable for test input im not sure we even need this...

    def get_player_turn(self):
        """
        Gets current turn from game
        :return:
        """
        self.turn = self.game.turn
        # for reading from our actual board not applicable for test input

    def possible_lead_piece_to_select(self, row_key, column_detail):
        row_num = self.convert_row_string_int(row_key)
        col_num = column_detail['colNum']
        piece = self.translate_piece_value_for_output(row_num, col_num)

        for direction in self.move_directions:
            direction_tuple = self.move_directions.get(direction)

            new_row = self.convert_row_string_int(row_key) + direction_tuple[0]
            new_col_num = col_num + self.calc_new_direction_coords(row_num, direction_tuple)
            new_row_key = self.convert_row_string_int(new_row)

            try:
                space_value = self.game.game_board[new_row_key][new_col_num]['color']
                if space_value is None:
                    # piece can move
                    pieces = (piece, piece)
                    # generate single piece inline move
                    self.move("i", pieces, direction)
                    self.possible_moves_single.add(("i", pieces, direction, new_row_key, new_col_num))

                    self.possible_multiple_piece_inline_groups(direction, row_key, col_num, new_row, new_col_num)

                opposite_color = self.get_opposite_color(self.turn)
                if space_value == opposite_color:

                    sumito_groupings = 2
                    while (sumito_groupings < 4):
                        num_of_adj_selected_piece = self.get_num_of_adj_pieces(self.turn, row_key, col_num, direction, sumito_groupings)

                        opposite_direction = self.opposite_direction[direction]
                        num_of_adj_opposing_pieces = self.get_num_of_adj_pieces("white", new_row_key, new_col_num, opposite_direction, sumito_groupings)

                        if num_of_adj_selected_piece > num_of_adj_opposing_pieces:
                            # getting row and col of space where sumito'ed piece is going to end up
                            sumito_row_num = self.convert_row_string_int(new_row_key) + direction_tuple[0]
                            sumito_row_key = self.convert_row_string_int(sumito_row_num)
                            sumito_col_num = self.calc_new_direction_coords(row_num, direction_tuple) + new_col_num

                            # gets the leading piece of the opposing color
                            new_row_num = self.convert_row_string_int(new_row_key)
                            new_piece = self.translate_piece_value_for_output(new_row_num, new_col_num)

                            # gets the 2nd piece to the leading piece
                            opposite_dir_coords = self.move_directions[opposite_direction]
                            opposite_dir_coords = (opposite_dir_coords[0], self.calc_new_direction_coords(new_row_num, opposite_dir_coords))
                            second_place_piece_row_num = new_row_num + opposite_dir_coords[0]
                            second_place_piece_col_num = new_col_num + opposite_dir_coords[1]
                            second_place_piece = self.translate_piece_value_for_output(second_place_piece_row_num, second_place_piece_col_num)

                            pieces = (new_piece, second_place_piece, self.sumito_trailing_piece)

                            self.possible_moves_sumito.add(("i", pieces, direction, sumito_row_key, sumito_col_num))

                        sumito_groupings += 1

                    # self.possible_2_piece_inline_groups(piece, direction, row_key, col_num, new_row, new_column)
                    # Piece may be able to move check further
                    # check for groups and oppo
                    # nent group sizes
                else:
                    pass
                    # piece cannot move
                    # move on to next piece
            except IndexError:
                print("outside board area")
        # from current board
        # if piece has space to move into
        # generate move then check for 2 piece groups with pre move layout
        # if is next to opponent color
        # check for 2 piece groups
        # else move on to next piece

    def perform_sumito(self, direction, row_key, col_num, pushed_piece_row_key, pushed_piece_col_num):


        # if group adjacent to opponents piece check if opponents pieces in line are >=
        # else move on to next piece
        # if not >= verify space behind opponent group is empty or not part of the board
        # else move on to next piece
        pass

    def get_num_of_adj_pieces(self, piece_color, row_key, col_num, direction, sumito_grouping=2):
        """

        :param piece_color: a string, the color of the adjacent pieces to get
        :param row_key: a string
        :param col_num: an int
        :param direction: a tuple
        :param sumito_grouping: an int, the number of grouped pieces to perform a sumito, set to 2 by default
        :return:
        """
        row_num = self.convert_row_string_int(row_key)
        opposite_dir = self.move_directions[self.opposite_direction[direction]]
        processed_opposite_dir = (opposite_dir[0], self.calc_new_direction_coords(row_num, opposite_dir))

        new_row_num = processed_opposite_dir[0] + row_num
        new_row_key = self.convert_row_string_int(new_row_num)
        new_col_num = processed_opposite_dir[1] + col_num

        num_of_adj_pieces = 0
        try:
            if self.updated_game_board[new_row_key][new_col_num]["color"] == piece_color:
                self.sumito_trailing_piece = self.translate_piece_value_for_output(new_row_num, new_col_num)
                num_of_adj_pieces += 1

                new_row_num = processed_opposite_dir[0] + new_row_num
                new_row_key = self.convert_row_string_int(new_row_num)
                new_col_num = self.calc_new_direction_coords(new_row_num, processed_opposite_dir) + new_col_num

                if self.updated_game_board[new_row_key][new_col_num]["color"] == piece_color and sumito_grouping == 3:
                    self.sumito_trailing_piece = self.translate_piece_value_for_output(new_row_num, new_col_num)
                    num_of_adj_pieces += 1
        except IndexError:
            print("Sumito check out of board area")
            return num_of_adj_pieces

        return num_of_adj_pieces

    def translate_piece_value_for_output(self, row_num, col_num):
        """
        Translates piece from internal coordinates to notation as required by game board coordinate system.
        :param row_num: an int
        :param col_num: an int
        :return:
        """
        ASCII_ALPHABET_OFFSET = 8
        ZERO_INDEX_OFFSET = 1

        TOP_ROW = 0
        UPPER_HALF = range(1, 4 + ZERO_INDEX_OFFSET)

        num_of_cols = self.game.calculate_row_length(row_num)

        # if the string row_key is passed, then it is converted to an int representing the row
        if type(row_num) != int:
            print("translate_piece_value_for_output passed wrong row_num value type")
            row_num = self.convert_row_string_int(row_num)

        if row_num == TOP_ROW:
            col_coord = num_of_cols + col_num
        elif row_num in UPPER_HALF:
            col_coord = (num_of_cols - (row_num * 2)) + col_num
        else:
            col_coord = col_num + ZERO_INDEX_OFFSET

        row_coord = chr((ASCII_ALPHABET_OFFSET - row_num) + 65)
        return row_coord + str(col_coord)

    def possible_multiple_piece_inline_groups(self, direction, row_key, col_num, new_row, new_column):
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

        # if adjacent_piece_val == self.turn:
        # check for adjacent pieces
        # if second piece adjacent select check for empty space to move into
        # generate move
        # if space to move into sidestep
        # generate move
        # check for third piece with pre move layout
        # else check if group bigger than opponents group
        pass

    def is_valid_adjacent_piece(self, opposite_adj_row_key, opposite_adj_col_num):
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
            print("Adjacent 2nd piece out of board area")
            return False

    @staticmethod
    def move(move_type, pieces, direction):
        """
        Outputs move in move notation.
        :param move_type: i or s: char
        :param pieces: tuple: front and end piece locations
        :param direction:
        :return:
        """
        # print(f"{move_type}-{pieces[0]}-{pieces[1]}-{direction}")
        # if previous checks pass create move notation and output move
        # call new board
        pass

    def create_piece_list_for_current_turn(self):
        # create an image of board before changes
        self.updated_game_board = deepcopy(self.game.game_board)

        for row_key in self.game.game_board:
            row = self.game.game_board[row_key]
            for column_detail in row:
                # if "white" in column_detail.values():
                #     print(column_detail)
                if self.turn in column_detail.values():
                    self.possible_lead_piece_to_select(row_key, column_detail)

    def update_board(self):

        print("===== (Debug) 1-piece moves =====")
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

        # debug
        print("===== (Debug) 2-piece moves =====")
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

        # debug
        print("===== (Debug) 3-piece moves =====")
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

        # debug
        print("===== (Debug) Sumito 3 push-1-and-2 moves =====")
        for move in self.possible_moves_sumito:
            # only for single piece moves
            if move[0] == 'i':

                leading_piece_coords = self.translate_single_piece_to_board_notation(move[1][0])
                second_place_piece_coords = self.translate_single_piece_to_board_notation(move[1][1])
                trailing_piece_coords = self.translate_single_piece_to_board_notation(move[1][2])

                opposing_color = self.get_opposite_color(self.turn)
                color_of_second_piece = self.updated_game_board[second_place_piece_coords[0]][second_place_piece_coords[1]]["color"]

                try:
                    # push opposing piece
                    self.updated_game_board[move[3]][move[4]]["color"] = opposing_color

                except IndexError:
                    # shift pieces as piece has been pushed off game board
                    print(f"{opposing_color.title()} piece pushed off the board!")

                else:
                    self.updated_game_board[second_place_piece_coords[0]][second_place_piece_coords[1]]["color"] = self.turn

                finally:
                    # replaces leading piece with the color of the piece behind it
                    self.updated_game_board[leading_piece_coords[0]][leading_piece_coords[1]]["color"] = color_of_second_piece

                    # removes trailing piece
                    self.updated_game_board[trailing_piece_coords[0]][trailing_piece_coords[1]]["color"] = None

                self.output_board()
                # resets board to before move
                self.updated_game_board = deepcopy(self.game.game_board)

    def translate_external_coords_to_internal_coords(self, piece_coord: str) -> tuple:
        ASCII_OFFSET = 65
        NUM_OF_ROWS_OFFSET = 8

        row_letter = piece_coord[0]

        row_num = (ord(row_letter) - ASCII_OFFSET - NUM_OF_ROWS_OFFSET) * -1
        col_num = self.calculate_column(row_num, int(piece_coord[1]))

        if row_num < 0:
            print("Out of range coordinates passed to transate_external_coords_to_internal_coords")

        row_key = self.convert_row_string_int(row_num)
        return (row_key, col_num)

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
            print("calc_new_direction_coords passed wrong row_num value type")
            row_num = self.convert_row_string_int(row_num)

        if row_num in UPPER_HALF:
            # checks for SE movement for pieces in the middle row
            if row_num == MIDDLE_ROW and new_row_dir == 1:
                if new_col_dir == 1:
                    new_col_dir = 0

            # checks for NE movement
            elif new_row_dir == -1:
                if new_col_dir == 1:
                    new_col_dir = 0

            # checks for SW movement
            elif new_row_dir == 1:
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

    def output_board(self):
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
        #print(sorted(blacks) + sorted(whites))
        self.print_to_text_file(sorted(blacks) + sorted(whites), "test1.board")

    def text_output_moves(self):
        """
        Outputs move in move notation.
        :param move_type: i or s: char
        :param pieces: tuple: front and end piece locations
        :param direction:
        :return:
        """
        possible_inline_moves = set().union(self.possible_moves_single).union(self.possible_moves_double)\
            .union(self.possible_moves_triple)

        for i in possible_inline_moves:
            move_type = i[0]
            pieces = i[1]
            direction = i[2]
            #print(f"{move_type}-{pieces[0]}-{pieces[1]}-{direction}")

        for i in self.possible_moves_sumito:
            move_type = i[0]
            pieces = i[1][1], i[1][1]
            direction = i[2]

    @staticmethod
    def print_to_text_file(item, path):

        item = str(item)
        item = item.replace('[', '').replace(']', '').replace(' ', '').replace("'", '')
        with open(path, "a") as file:
            file.write(item)
            file.write("\n")


s = StateSpaceGenerator()
s.read_test_input("Test1.input")
s.translate_test_input_to_board_notation()
s.create_piece_list_for_current_turn()
s.update_board()
s.text_output_moves()
