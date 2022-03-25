import time
from random import Random
from heuristics import KatsHeuristic
import board_query
from move import *
from converter import *


from state_space_generator import *

#
# def center(board, turn):
#     """
#     gets average of distance from center of all pieces of provided color
#     :param board: gameboard array
#     :param color: player whose turn it is color
#     :return: float
#     """
#     proximity_counter = 0
#     pieces = 0
#     # 9 rows 9 columns center is E5 or board notation row 4 column 4
#     for row in board.items():
#         row_number = Converter.convert_row_to_string_or_int(row[0])
#         row = row[1]
#         for place in row:
#             if place['color'] == turn:
#                 pieces += 1
#                 col_dist = abs(place['colNum'] - 4)
#                 row_dist = abs(int(row_number) - 4)
#                 total = col_dist + row_dist
#                 proximity_counter += total
#     proximity_counter = proximity_counter/pieces
#     return proximity_counter
#

def get_opposite_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'

#
# def heuristic(state):
#     center_value = center(state[1], state[2]) - center(state[1], get_opposite_color(state[2]))
#     return center_value


test_board = {'row0': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row1': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row2': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row3': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row4': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 8, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row5': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row6': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row7': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row8': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}]}
turn = "black"


class Minimax:

    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.pruned = 0

    def alpha_beta(self, state):
        start = time.perf_counter()
        a, b, value = float('-inf'), float('inf'), float('-inf')
        generator = StateSpaceGenerator(state[1], state[2])
        next_states = generator.run_generation()
        next_states_values_dict = {}
        for next_state in next_states:
            print(next_state[0])
            next_depth_state = next_state[0], next_state[1], self.get_opposite_color(state[2]), state[3] + 1
            value = max(value, self.min_value(next_depth_state, a, b))
            a = max(a, value)
            next_states_values_dict.update({value: next_depth_state})

        max_val = max([x for x in next_states_values_dict.keys()])
        options = [x for x in next_states_values_dict.items() if x[0] == max_val]

        choice = self.random_choice(options)
        print(time.perf_counter() - start)
        print(self.pruned)
        return choice[1][0], choice[1][1]    # returns updated game board to game.py on line 249 within game.py

    def max_value(self, depth_state, a, b):
        if self.is_terminal(depth_state):  # if depth is equal to max depth
            return self.get_value(depth_state)

        v = float('-inf')

        next_states = self.get_next_states(depth_state)
        for next_state in next_states:
            next_depth_state = next_state[0], next_state[1], self.get_opposite_color(depth_state[2]), depth_state[3] + 1
            v = max(v, self.min_value(next_depth_state, a, b))
            if v >= b:
                self.pruned += 1
                return v
            a = max(a, v)
        return v

    def min_value(self, depth_state, a, b):
        if self.is_terminal(depth_state):  # if depth is equal to max depth
            return self.get_value(depth_state)

        v = float('inf')

        next_states = self.get_next_states(depth_state)
        for next_state in next_states:
            next_depth_state = next_state[0], next_state[1], self.get_opposite_color(depth_state[2]), depth_state[3] + 1
            v = min(v, self.max_value(next_depth_state, a, b))
            if v <= a:
                self.pruned += 1
                return v
            b = min(b, v)
        return v


    @staticmethod
    def get_opposite_color(color):
        if color == 'black':
            return 'white'
        else:
            return 'black'

    def is_terminal(self, depth_state):
        if depth_state[3] == self.max_depth:
            return True
        return False

    @staticmethod
    def get_value(state):
        return KatsHeuristic.weighted_heuristic(state)

    @staticmethod
    def random_choice(list):
        choice_index = Random.randint(Random(), 0, len(list) - 1)
        return list[choice_index]


    @staticmethod
    def get_next_states(state):
        generator = StateSpaceGenerator(state[1], state[2])
        next_states = generator.run_generation()
        return next_states


