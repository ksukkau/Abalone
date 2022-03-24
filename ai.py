import time
from random import Random

from game import *
from state_space_generator import *
# TODO minimax
# TODO Alpha beta pruning
# TODO transposition table
# TODO heuristics


test_board = {'row0': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}], 'row1': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}], 'row2': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 6, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}], 'row3': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 6, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}], 'row4': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 6, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 8, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}], 'row5': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 6, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}], 'row6': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 6, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}], 'row7': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 5, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}], 'row8': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}, {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}]}
turn = "black"


# depth limited minimax search
# minmax needs to be called when turn is completed
class Minimax:

    def __init__(self, max_depth=2):
        self.max_depth = max_depth
        # trans table goes here too

    def minimax_decision(self, board, turn_color):
        start = time.perf_counter()
        depth_state = board, turn_color, 0
        generator = StateSpaceGenerator(depth_state[0], depth_state[1])
        next_states = generator.run_generation()  # tuple of (move, board)
        min_values = {}

        for state in next_states[:3]:
            next_depth_state = state[1], self.get_opposite_color(depth_state[1]), depth_state[2]+1
            #print(self.min_value(next_depth_state))
            min_values.update({self.min_value(next_depth_state): state})
            print(self.min_value(next_depth_state))
        stop = time.perf_counter()
        print(stop - start)

        max_val = max(min_values.keys())
        print(min_values)
        max_states = [k for k, v in min_values.items() if k == max_val]
        choice = max_states[Random.randint(Random(), 0, len(max_states)-1)]
        #move = next_states[next_states.index(choice)][0]

        #return move

    def max_value(self, depth_state):

        if self.is_terminal(depth_state): # if depth is equal to max depth
            return self.get_value(depth_state[0], depth_state[1])

        v = float('-inf')

        generator = StateSpaceGenerator(depth_state[0], depth_state[1])
        next_states = generator.run_generation()  # tuple of (move, board)

        for state in next_states:
            next_depth_state = state[1], self.get_opposite_color(depth_state[1]), depth_state[2] + 1
            v = max(v, self.min_value(next_depth_state))
        return v

    def min_value(self, depth_state):

        if self.is_terminal(depth_state):  # if depth is equal to max depth
            return self.get_value(depth_state[0], depth_state[1])  # this is the heuristics function

        v = float('inf')

        generator = StateSpaceGenerator(depth_state[0], depth_state[1])
        next_states = generator.run_generation()  # tuple of (move, board)

        for state in next_states:
            next_depth_state = state[1], self.get_opposite_color(depth_state[1]), depth_state[2] + 1
            v = min(v, self.max_value(next_depth_state))
        return v

    @staticmethod
    def get_opposite_color(color):
        if color == 'black':
            return 'white'
        else:
            return 'black'

    def is_terminal(self, depth_state):
        if depth_state[2] == self.max_depth:
            return True
        return False

    def get_value(self, board, current_turn):
        return Random.randint(Random(), 1, 100)
        # call heuristic here

    def alpha_beta(self):
        pass



m = Minimax()
print(m.minimax_decision(test_board, turn))

