from game import *
# TODO minimax
# TODO Alpha beta pruning
# TODO transposition table
# TODO heuristics

####################################### KATS HEURISTIC ##########################################
def heuristic(board):
    center_proximity = board.query.center_proximity(False) - board.query.center_proximity(True)

    # cohesion
    grouping = 0
    if abs(center_proximity) > 2:
        cohesion = len(list(board.query.populations(False))) - len(list(board.query.populations(True)))

    # number of marbles
    marbles = 0
    if abs(center_proximity) < 1.8:
        marbles = board.query.marbles(True, True) * 100 - board.query.marbles(False, True) * 100

    return center_proximity + cohesion + marbles