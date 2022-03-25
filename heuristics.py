from board_query import *


def get_opposite_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'


class KatsHeuristic:

    @staticmethod
    def heuristic(state):
        center_value = center(state[1], state[2]) - center(state[1], get_opposite_color(state[2]))

        move = state[0]
        if len(move[1]) == 3:
            push = 100
        else:
            push = 0
        # #
        #
        # grouping = 0
        # if abs(center_value) > 2:
        #     grouping = groups(board, turn) - groups(board, turn)
            # return 1/ grouping
        #
        marbles = 0
        if abs(center_value) < 1.8:
            marbles = pieces(state[1], state[2]) - pieces(state[1], get_opposite_color(state[2]))

        return center_value + marbles + push

