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

        return center_value #+ marbles #  + push

    @staticmethod
    def weighted_heuristic(state):
        score_weight = 0.1
        center_weight = 0.1
        push_weight = 0.1
        group_weight = 0.1

        # piece_count = move_piece_count(state)
        # print("piece count:" + str(piece_count))
        score = pieces(state[1],state[2]) - pieces(state[1], get_opposite_color(state[2]))
        #print("score: " + str(score))
        center_value = center(state[1], state[2]) - center(state[1], get_opposite_color(state[2]))
        #print("center: " + str(center_value))
    #   group = groups(state[1], state[2]) - groups(state[1], get_opposite_color(state[2]))
        push = push_eval(state)
        #print("push:" + str(push))

        return score_weight * score + center_weight * center_value + push_weight * push


