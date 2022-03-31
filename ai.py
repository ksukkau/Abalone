from random import Random

from heuristics import KatsHeuristic

from state_space_generator import *


class Minimax:

    def __init__(self, max_depth=2):
        self.max_depth = max_depth
        self.pruned = 0

    def alpha_beta(self, state):
        a, b, value = float('-inf'), float('inf'), float('-inf')
        generator = StateSpaceGenerator(state[1], state[2])
        next_states = generator.run_generation()
        next_states_values_dict = {}
        for next_state in next_states:
            # print(next_state[0])
            next_depth_state = next_state[0], next_state[1], self.get_opposite_color(state[2]), state[3] + 1
            value = max(value, self.min_value(next_depth_state, a, b))
            a = max(a, value)
            next_states_values_dict.update({value: next_depth_state})

        # print([x for x, y in next_states_values_dict.items()])
        max_val = min([x for x in next_states_values_dict.keys()])  # finds the lowest valued item in list
        options = [x for x in next_states_values_dict.items() if
                   x[0] == max_val]  # finds all item with same value as max_val
        # print(options)
        choice = self.random_choice(options)  # randomly selects move from options
        print(self.pruned)  # prints number of nodes pruned
        return choice[1][0], choice[1][1]  # returns updated game board to game.py on line 249 within game.py

    def max_value(self, depth_state, a, b):
        if self.is_terminal(depth_state):  # if depth is equal to max depth
            value = self.get_value(depth_state)
            # print("Max value", value)
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
            # print("Min value", value)
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
