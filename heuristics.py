from board_query import *


def get_opposite_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'


class KatsHeuristic:
    # Currently unused left in place for testing purposes
    #
    # @staticmethod
    # def heuristic(state):
    #
    #
    #     center_value = center(state[1], state[2]) - center(state[1], get_opposite_color(state[2]))
    #
    #     move = state[0]
    #     if len(move[1]) == 3:
    #         push = 100
    #     else:
    #         push = 0
    #     # #
    #     #
    #     # grouping = 0
    #     # if abs(center_value) > 2:
    #     #     grouping = groups(board, turn) - groups(board, turn)
    #         # return 1/ grouping
    #     #
    #     marbles = 0
    #     if abs(center_value) < 1.8:
    #         marbles = pieces(state[1], state[2]) - pieces(state[1], get_opposite_color(state[2]))
    #
    #     return center_value #+ marbles #  + push

    @staticmethod
    def weighted_heuristic(state):
        score_weight = 10
        center_weight = 5
        push_weight = 9
        group_weight = 1
        move_size = 3

        # piece_count = move_piece_count(state)
        # print("piece count:" + str(piece_count))
        score = pieces(state[1], state[2]) - pieces(state[1], get_opposite_color(state[2]))
        #print("Score", score)
        center_value = center(state[1], state[2]) - center(state[1], get_opposite_color(state[2]))
        #print("centerValue ", center_value)
        group = len(groups(state[1], state[2])) - len(groups(state[1], get_opposite_color(state[2])))

        push = push_eval(state)
        #print("Push", push)
        int_value = int(score_weight * score + center_weight * center_value + push_weight * push + group * group_weight)
        return int_value


