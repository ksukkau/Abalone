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
        self.possible_moves = set()
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
        row_num = int(row_key.replace("row", ''))
        col_num = column_detail['colNum']
        piece = self.translate_piece_value_for_output(row_num, col_num)

        for direction in self.move_directions:
            direction_tuple = self.move_directions.get(direction)

            new_row = int(row_key.replace("row", '')) + direction_tuple[0]
            new_column = col_num + self.calc_new_direction_coords(row_num, direction_tuple)
            new_row_key = "row" + str(new_row)

            try:
                space_value = self.game.game_board[new_row_key][new_column]['color']
                if space_value is None:
                    # piece can move
                    pieces = (piece, piece)
                    # generate single piece inline move
                    self.move("i", pieces, direction)
                    self.possible_moves.add(("i", pieces, direction, new_row_key, new_column))
                    self.possible_2_piece_inline_groups(piece, direction, row_key, col_num, new_row, new_column)
                elif space_value == "white":
                    pass
                    # self.possible_2_piece_inline_groups(piece, direction, row_key, col_num, new_row, new_column)
                    # Piece may be able to move check further
                    # check for groups and opponent group sizes
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

    @staticmethod
    def calc_new_direction_coords(row_num, direction):
        """
        Calculate the coordinates of the new direction given the current row and column of the game piece, as well as
        the direction of movement. Required due to the varying columns on each row on the game board because of the
        hexagonal shaped game board.
        :param row_num: an int, representing the row of the selected game piece
        :param direction: an tuple, containing the new movement as (x,y) or (row, col)
        :return: a int, containing the direction of the new movement along the column (west to east vector)
        """
        ZERO_INDEX_OFFSET = 1
        UPPER_HALF = range(1, 4 + ZERO_INDEX_OFFSET)
        MIDDLE_ROW = 4

        new_row_dir = direction[0]
        new_col_dir = direction[1]

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

    def translate_piece_value_for_output(self, row, col):
        """
        Translates piece from internal coordinates to notation as required by game board coordinate system.
        :param row:
        :param col:
        :return:
        """
        ASCII_ALPHABET_OFFSET = 8
        ZERO_INDEX_OFFSET = 1

        TOP_ROW = 0
        UPPER_HALF = range(1, 4 + ZERO_INDEX_OFFSET)

        num_of_cols = self.game.calculate_row_length(row)

        if row == TOP_ROW:
            col_coord = num_of_cols + col
        elif row in UPPER_HALF:
            col_coord = (num_of_cols - (row * 2)) + col
        else:
            col_coord = col + ZERO_INDEX_OFFSET

        row_coord = chr((ASCII_ALPHABET_OFFSET - row) + 65)
        return row_coord + str(col_coord)

    def possible_2_piece_inline_groups(self, piece, direction, row_key, col_num, new_row, new_column):
        row_num = int(row_key.replace("row", ''))
        opposite_direction = {
            "NE": "SW",
            "E": "W",
            "SE": "NW",
            "SW": "NE",
            "W": "E",
            "NW": "SE"
        }
        print(piece)
        print(direction)
        o_direction = opposite_direction.get(direction)
        print(o_direction)
        direction_tuple = self.move_directions.get(o_direction)

        new_row = int(row_key.replace("row", '')) + direction_tuple[0]
        new_column = col_num + self.calc_new_direction_coords(row_num, direction_tuple)
        new_row_key = "row" + str(new_row)
        space_value = self.game.game_board[new_row_key][new_column]['color']
        if space_value == "black":
            print(new_row, self.game.game_board[new_row_key][new_column])
        # check for adjacent pieces
        # if second piece adjacent select check for empty space to move into
        # generate move
        # if space to move into sidestep
        # generate move
        # check for third piece with pre move layout
        # else check if group bigger than opponents group
        pass

    def check_for_3_piece_groups(self, piece, row_key, col_num, new_row, new_column):
        # if check for pieces adjacent and in line with 2 piece groups
        # if space to move into inline
        # generate move
        # if space to move into sidestep
        # generate move
        # if opponents adjacent check for piece group bgger

        # 3 is max group size
        pass

    def check_for_sumito_opponents(self):
        # if group adjacent to opponents piece check if opponents pieces in line are >=
        # else move on to next piece
        # if not >= verify space behind opponent group is empty or not part of the board
        # else move on to next piece
        pass

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
        # ("i", pieces, direction, new_row_key, new_column)

        for move in self.possible_moves:
            if move[0] == 'i':
                print(move)
                # move front piece up
                self.updated_game_board[move[3]][move[4]]['color'] = self.turn
                # remove back piece
                location = self.translate_single_piece_to_board_notation(move[1][1])
                self.updated_game_board[location[0]][location[1]]['color'] = None
                self.output_board()
                # resets board to before move
                self.updated_game_board = deepcopy(self.game.game_board)

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
        else:
            print("Invalid value passed. Argument must be a string or an integer.")

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

        print(sorted(blacks) + sorted(whites))


s = StateSpaceGenerator()
s.read_test_input("Test1.input")
s.translate_test_input_to_board_notation()
s.create_piece_list_for_current_turn()
s.update_board()
