import time
from random import Random
from heuristics import KatsHeuristic
import board_query
from move import *
from converter import *


from state_space_generator import *


def get_opposite_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'


test_board = {'row0': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row1': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row2': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row3': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row4': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 8, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row5': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row6': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row7': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row8': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}]}
turn = "black"


class Minimax:

    def __init__(self, max_depth=2):
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

        #print([x for x, y in next_states_values_dict.items()])
        max_val = min([x for x in next_states_values_dict.keys()])
        options = [x for x in next_states_values_dict.items() if x[0] == max_val]
        #print(options)
        choice = self.random_choice(options)
        print(time.perf_counter() - start)
        print(self.pruned)
        return choice[1][0], choice[1][1]    # returns updated game board to game.py on line 249 within game.py

    def max_value(self, depth_state, a, b):
        if self.is_terminal(depth_state):  # if depth is equal to max depth
            value = self.get_value(depth_state)
            #print("Max value", value)
            return value

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
            value = self.get_value(depth_state)
            #print("Min value", value)
            return value

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
