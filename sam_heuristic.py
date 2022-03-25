from board_query import *


def get_opposite_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'


class SamsHeuristic:

    @staticmethod
    def heuristic(state):
        center_value = center(state[1], state[2])
        current_turn_center_value = center_value * (40 - state[3])

        current_piece_value = pieces(state[1], state[2]) - pieces(state[1], get_opposite_color(state[2]))

        return current_turn_center_value + current_piece_value * state[3]
