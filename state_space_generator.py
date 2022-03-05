import math
from settings import *
from tkinter import *
import tkinter as tk


class StateSpaceGenerator:
    """
    Encapsulates the methods required to generate the state space at any given game state.
    """
    def __init__(self):
        self.turn = ""
        self.board = ""
        self.possible_boards = None
        self.group = None

    def read_test_input(self, path):
        with open(path, 'r') as input_file:
            self.turn = input_file.readline()
            self.board = input_file.readline()

    def get_current_board(self):
        pass # for reading from our actual board not applicable for test input

    def get_player_turn(self):
        pass # for reading from our actual board not applicable for test input

    def possible_lead_piece_to_select(self):
        #from current board
        #if piece has space to move into
        # generate move then check for 2 piece groups with pre move layout
        # if is next to opponent color
        #check for 2 piece groups
        #else move on to next piece
        pass

    def possible_2_piece_groups(self):
        #check for adjacent pieces
        #if second piece adjacent select check for empty space to move into
        #geneerate move
        #check for third piece with pre move layout
        #else check if group bigger than opponents group
        pass

    def check_for_3_piece_groups(self):
        #check for pieces adjacent and in line with 2 piece groups
        #if space to move into
        #generate move
        #if opponents check for piece group bgger

        # 3 is max group size
        pass

    def check_if_piece_group_bigger_than_opponents(self):
        #if group adjacent to opponents piece check if opponents pieces in line are >=
        #else move on to next piece
        #if not >= verify space behind opponent group is empty or not part of the board
        #else move on to next piece
        pass

    def move(self):
        #if previous checks pass create move notation and output move
        #call new board(
        pass

    def new_board(self):
        # board state after move
        # stored in a list
        pass



StateSpaceGenerator.read_test_input("Test1.input")
