import math
from settings import *
from tkinter import *
import tkinter as tk
from game import *


class StateSpaceGenerator:
    """
    Encapsulates the methods required to generate the state space at any given game state.
    """
    def __init__(self):
        self.turn = ""
        self.board_text = ""
        self.possible_boards = None
        self.group = None
        self.game = GameBoard()

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

    def translate_test_input_to_board_notation(self):
        """
        Creates a game board array based on test input.
        :return: None
        """
        self.game.initialize_game_board_array()
        rows = {
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
        colors = {
            "b": "black",
            "w": "white"
        }

        piece_list = self.board_text.split(',')
        for item in piece_list:
            row = rows[item[0]]
            row_key = "row" + str(row)
            col = int(item[1])
            color = colors[item[2]]
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

    def create_piece_list_for_current_turn(self):
        for row_key in self.game.game_board:
            row = self.game.game_board[row_key]
            for column_detail in row:
                if self.turn in column_detail.values():
                    self.possible_lead_piece_to_select(row_key, column_detail)

    def possible_lead_piece_to_select(self, row_key, column_detail):
        piece = self.translate_piece_value_for_output(int(row_key.replace("row", '')), column_detail["colNum"])
        print(piece)
        move_directions = {
            "NE": (-1, 1),
            "E": (0, 1),
            "SE": (1, 1),
            "SW": (1, -1),
            "W": (0, -1),
            "NW": (-1, -1)
        }
        for direction in move_directions:
            direction_tuple = move_directions.get(direction)
            new_row = int(row_key.replace("row", '')) + direction_tuple[0]
            new_row_key = "row" + str(new_row)
            new_column = column_detail["colNum"] + direction_tuple[1]
            try:
                space_value = self.game.game_board[new_row_key][new_column]['color']
                if space_value is None:
                    print(space_value)
                    # piece can move
                    pieces = (piece, piece)
                    self.move("i", pieces, direction)
                    #change this to generate move and board, then check for groups
                elif space_value == "white":
                    #Piece may be able to move check further
                    pass
                    #check for groups and opponent group sizes
                else:
                    pass
                    # piece cannot move
                    # move on to next piece
            except:
                print("outside board area")
        # from current board
        # if piece has space to move into
        # generate move then check for 2 piece groups with pre move layout
        # if is next to opponent color
        # check for 2 piece groups
        # else move on to next piece

    def translate_piece_value_for_output(self, row, col):
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

    def possible_2_piece_groups(self):
        # check for adjacent pieces
        # if second piece adjacent select check for empty space to move into
        # generate move
        # if space to move into sidestep
        # generate move
        # check for third piece with pre move layout
        # else check if group bigger than opponents group
        pass

    def check_for_3_piece_groups(self):
        # if check for pieces adjacent and in line with 2 piece groups
        # if space to move into inline
        # generate move
        # if space to move into sidestep
        # generate move
        # if opponents adjacent check for piece group bgger

        # 3 is max group size
        pass

    def check_if_piece_group_bigger_than_opponents(self):
        #if group adjacent to opponents piece check if opponents pieces in line are >=
        #else move on to next piece
        #if not >= verify space behind opponent group is empty or not part of the board
        #else move on to next piece
        pass

    @staticmethod
    def move(move_type, pieces, direction):
        print(f"{move_type}-{pieces[0]}-{pieces[1]}-{direction}")
        #if previous checks pass create move notation and output move
        #call new board
        pass

    def new_board(self):
        # board state after move
        # stored in a list
        pass



s = StateSpaceGenerator()
s.read_test_input("Test1.input")
s.translate_test_input_to_board_notation()
s.create_piece_list_for_current_turn()
