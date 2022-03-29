from game import *
from move import *
from converter import *

test_board = {'row0': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row1': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row2': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row3': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row4': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 8, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row5': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row6': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row7': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row8': [{'colNum': 0, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'color': None, 'selected': False, 'x_pos': None, 'y_pos': None}]}
turn = "black"


def center(board, color):
    """
    gets average of distance from center of all pieces of provided color
    :param board: gameboard array
    :param color: player whose turn it is color
    :return: float
    """
    proximity_counter = 0
    pieces = 0
    # 9 rows 9 columns center is E5 or board notation row 4 column 4
    for row in board.items():
        row_number = Converter.convert_row_to_string_or_int(row[0])
        row = row[1]
        for place in row:
            if place['color'] == color:
                pieces += 1
                col_dist = abs(place['colNum'] - 4)
                row_dist = abs(int(row_number) - 4)
                total = col_dist + row_dist
                proximity_counter += total
    proximity_counter = proximity_counter/pieces
    return proximity_counter


def pieces(board, color):
    """
    counts pieces of the color on the board
    :param board: gameboard array
    :param color: player whose turn it is color
    :return: int
    """
    piece_count = 0
    for row in board.items():
        row = row[1]
        for place in row:
            if place['color'] == color:
                piece_count += 1
    return piece_count


def groups(board, color):
    group_count = 1
    list_of_pieces = []
    for row in board.items():
        row_number = Converter.convert_row_to_string_or_int(row[0])
        row = row[1]
        for place in row:
            if place['color'] == color:
                spaces = Move.get_adj_spaces(row_number, place['colNum'])
                agjs = space_translation(board, spaces, color)
                #print(spaces)
                list_of_pieces.append((row_number, place['colNum']))
    #print(list_of_pieces)
    for i in range(len(list_of_pieces)-1):
        row = abs(list_of_pieces[i][0] - list_of_pieces[i+1][0])
        col = abs(list_of_pieces[i][1] - list_of_pieces[i+1][1])
        if row > 1 and col > 1:
            group_count += 1

    return group_count


def space_translation(board, adj_list, color):
    """
    finds any same color adjacent pieces to the current piece
    :param board:
    :param adj_list:
    :param color:
    :return:
    """
    adjs = []
    for item in adj_list:
        spot = Converter.external_notation_to_internal(item)
        for item in board[spot[0]]:
            if item['colNum'] == spot[1]:
                if item['color'] == color:
                    adjs.append(spot)


def push_eval(state):

    move = state[0]
    if len(move[1]) == 3:
        push = True
    else:
        push = False

    if push:
        # find distance of pushed piece from the edge
        piece_location = Converter.external_notation_to_internal(move[1][1])
        row_number = Converter.convert_row_to_string_or_int(piece_location[0])
        col_dist = abs(piece_location[1] - 4)
        row_dist = abs(int(row_number) - 4)
        total = col_dist + row_dist
        if total > 2:
            return 10
        else:
            return 2
    else:
        return 0


def move_piece_count(state):
    move_notation = state[0]
    if len(move_notation[1]) == 3:
        move = move_notation[1], move_notation[2]
    else:
        move = move_notation
    first_piece_location = Converter.external_notation_to_internal(move[1][0])
    first_row_number = Converter.convert_row_to_string_or_int(first_piece_location[0])
    last_piece_location = Converter.external_notation_to_internal(move[1][1])
    last_row_number = Converter.convert_row_to_string_or_int(last_piece_location[0])
    return abs(first_piece_location[1] - last_piece_location[1] + first_row_number - last_row_number)


class AllyCount:

    def __init__(self):
        self.ally_groups = []  # contains sets with the ally counts
        self.game_board = {}





#     print(adjs)
#
#
# #print(groups(test_board, "black"))
# print(groups(test_board, "white"))
#
# print(center(test_board, "black"))
# print(center(test_board, "white"))
# print(pieces(test_board, "black"))
# print(pieces(test_board, "white"))
#
