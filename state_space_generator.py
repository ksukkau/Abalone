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




StateSpaceGenerator.read_test_input("Test1.input")
