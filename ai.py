# TODO minimax
# TODO Alpha beta pruning
# TODO transposition table
# TODO heuristics

'''
Minimax
terminal test in pseudocode is max depth, start at depth 0,
starts with max then min so want to stop on a min value
min values come from the max value below them and is always backed up
arbitrary value for max (infinity)
quits when terminal test
get values are based on heuristic from nodes state
layer 0 is existing board
layer 1 is all boards generated from existing board
layer 2 is all boards generated for each board in layer 1
alpha beta pruning is added to minimax to improve
transposition table caches values from layer 2
node ordering is a good enhancement
sumitos are scoring moves and are likely more valuable - could be used for alpha beta pruning
3 marble moves - higher value also could be used for ordering nodes sumito down to 1 marble in order to order tree
'''




