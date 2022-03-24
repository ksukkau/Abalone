import time
from random import Random
from heuristics import *

from state_space_generator import *

# TODO minimax
# TODO Alpha beta pruning
# TODO transposition table
# TODO heuristics


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


# depth limited minimax search
# minmax needs to be called when turn is completed
class Minimax:

    def __init__(self, max_depth=2):
        self.max_depth = max_depth
        self.turn = ''
        self.pruned = 0
        # trans table goes here too

    # def set_maximizer_turn_color(self, turn_color):
    #     self.turn = turn_color

    # def minimax_decision(self, board, turn_color):
    #     depth_state = board, turn_color, 0
    #     generator = StateSpaceGenerator(depth_state[0], depth_state[1])
    #     next_states = generator.run_generation()
    #     min_values = {}
    #
    #     for state in next_states:
    #         next_depth_state = state[0], self.get_opposite_color(depth_state[1]), depth_state[2] + 1
    #         min_values.update({self.min_value(next_depth_state): state})
    #
    #     #print(min_values)
    #     max_val = max(min_values.keys())
    #
    #     max_states = [k for k, v in min_values.items() if k == max_val]
    #     choice = max_states[Random.randint(Random(), 0, len(max_states) - 1)]
    #     move = next_states[next_states.index(choice)][0]
    #
    #     return move

    def max_value(self, depth_state, a, b):
        if self.is_terminal(depth_state):  # if depth is equal to max depth
            return self.get_value(depth_state[1], depth_state[2])

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
            return self.get_value(depth_state[1], depth_state[2])

        v = float('-inf')

        next_states = self.get_next_states(depth_state)
        for next_state in next_states:
            next_depth_state = next_state[0], next_state[1], self.get_opposite_color(depth_state[2]), depth_state[3] + 1
            v = min(v, self.min_value(next_depth_state, a, b))
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
    def get_value(board, current_turn):
        return KatsHeuristic.heuristic(board, current_turn)

    # def alpha_beta(self, state, depth, a, b, maximizer):
    #     if depth == 0:
    #         return self.get_value(state, maximizer)
    #     if maximizer:
    #         value = float('-inf')
    #         next_states = self.get_next_states(state)
    #         for state in next_states:
    #             value = max(value, self.alpha_beta(state, depth - 1, a, b, False))
    #             if value >= b:
    #                 break
    #             a = max(a, value)
    #         return value
    #     else:
    #         value = float('inf')
    #         next_states = self.get_next_states(state)
    #         for state in next_states:
    #             value = min(value, self.alpha_beta(state, depth - 1, a, b, True))
    #             if value <= a:
    #                 break
    #             b = min(b, value)
    #         return value

    def alpha_beta(self, state):
        a, b, value = float('-inf'), float('inf'), float('-inf')
        next_states = self.get_next_states(state)
        next_states_values_dict = {}
        for next_state in next_states:
            next_depth_state = next_state[0], next_state[1], self.get_opposite_color(state[2]), state[3] + 1
            value = max(value, self.min_value(next_depth_state, a, b))
            a = max(a, value)
            next_states_values_dict.update({value: next_depth_state})
        for i in next_states_values_dict.items():
            print(i)

        return next_states_values_dict[value][1]  # returns updated game board to game.py on line 249 within game.py

    @staticmethod
    def get_next_states(state):
        generator = StateSpaceGenerator(state[1], state[2])
        next_states = generator.run_generation()
        return next_states

# commented out for integration testing with game.py
"""
m = Minimax()
depth = 2
# m.minimax_decision(test_board, turn)
# m.set_maximizer_turn_color(turn)
state = ["move", test_board, turn, 0]

m.alpha_beta(state)
#m.alpha_beta(state)
#print(m.alpha_beta(state, depth, float('-inf'), float('inf'), True))


#print(m.minimax_decision(test_board, turn))
"""