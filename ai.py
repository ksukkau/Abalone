from game import *
# TODO minimax
# TODO Alpha beta pruning
# TODO transposition table
# TODO heuristics


# depth limited minimax search
class Minimax:

    def __init__(self, state):
        self.state = state

    def minimax_decision(self):
        pass

    def max_value(self):
        pass

    def min_value(self):
        pass



# ####################################### KATS HEURISTIC ##########################################
# def heuristic(board):
#     center_proximity = board.query.center_proximity(False) - board.query.center_proximity(True)
#
#     # cohesion
#     grouping = 0
#     if abs(center_proximity) > 2:
#         grouping = len(list(board.query.populations(False))) - len(list(board.query.populations(True)))
#
#     # number of marbles
#     marbles = 0
#     if abs(center_proximity) < 1.8:
#         marbles = board.query.marbles(True, True) * 100 - board.query.marbles(False, True) * 100
#
#     return center_proximity + grouping + marbles
