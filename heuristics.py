from board_query import *


def get_opposite_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'


class KatsHeuristic:

    @staticmethod
    def heuristic(board, turn):
        center_value = center(board, turn) - center(board, get_opposite_color(turn))
        #

        grouping = 0
        if abs(center_value) > 2:
            grouping = groups(board, turn) - groups

        marbles = 0
        if abs(center_value) < 1.8:
            marbles = pieces(board, turn) - pieces(board, get_opposite_color(turn))

        return center_value + grouping + marbles
