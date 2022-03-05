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

    def read_test_input(self, path):
        with open(path, 'r') as input_file:
            self.turn = input_file.readline()
            self.board = input_file.readline()

    def get_current_board(self):
        pass # for reading from our actual board not applicable for test input

    def get_player_turn(self):
        pass # for reading from our actual board not applicable for test input

    def possible_lead_piece_to_select(self):
        #if piece has space to move into or is next to opponent color
        #else move on to next piece
        pass

    def possible_2_piece_groups(self):
        #check for adjacent pieces
        pass

    def check_for_3_piece_groups(self):
        #check for pieces adjacent and in line with 2 piece groups
        # 3 is max group size
        pass

    def check_if_piece_group_bigger_than_opponents(self):
        #if group adjacent to opponents piece check if opponents pieces in line are >=
        #else move on to next piece
        #if not >= verify space behind opponent group is empty or not part of the board
        #else move on to next piece
        pass

    def move(self):
        #if previous checks pass create move notation and redraw board
        pass

    def new_board(self):
        # board state after move
        pass



StateSpaceGenerator.read_test_input("Test1.input")
