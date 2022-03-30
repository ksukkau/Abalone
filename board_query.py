from game import *
from move import *
from converter import *

test_board = {'row0': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row1': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row2': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row3': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row4': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 8, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row5': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 7, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row6': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': 'white', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': 'black', 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 6, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row7': [{'colNum': 0, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 5, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None}],
              'row8': [{'colNum': 0, 'turn_color': "black", 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 1, 'turn_color': "black", 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 2, 'turn_color': None, 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 3, 'turn_color': "black", 'selected': False, 'x_pos': None, 'y_pos': None},
                       {'colNum': 4, 'turn_color': "black", 'selected': False, 'x_pos': None, 'y_pos': None}]}
turn = "black"


def center(board, color):
    """
    gets average of distance from center of all pieces of provided turn_color
    :param board: gameboard array
    :param color: player whose turn it is turn_color
    :return: float
    """
    proximity_counter = 0
    pieces = 0
    # 9 rows 9 columns center is E5 or board notation row 4 column 4
    for row in board.items():
        row_number = Converter.convert_row_to_string_or_int(row[0])
        row = row[1]
        for place in row:
            if place['turn_color'] == color:
                pieces += 1
                col_dist = abs(place['colNum'] - 4)
                row_dist = abs(int(row_number) - 4)
                total = col_dist + row_dist
                proximity_counter += total
    proximity_counter = proximity_counter/pieces
    return proximity_counter


def pieces(board, color):
    """
    counts pieces of the turn_color on the board
    :param board: gameboard array
    :param color: player whose turn it is turn_color
    :return: int
    """
    piece_count = 0
    for row in board.items():
        row = row[1]
        for place in row:
            if place['turn_color'] == color:
                piece_count += 1
    return piece_count


def groups(board: dict, turn_color: str) -> list:
    """
    Returns the ally count of the specified color for a given game board state.
    :param board: a dictionary, of the game board
    :param turn_color: a string, the color to perform the ally count for
    :return: a list of lists, containing the ally count groupings
    """
    ally_count = []  # contains all of the groupings of ally counts
    ally_count_grouping = []  # temporarily stores the current ally count grouping
    neighbours_to_check = set()
    already_checked = set()

    for row in board:
        for piece in board[row]:

            if piece["turn_color"] == turn_color and (row, piece["colNum"]) not in already_checked:

                ally_count_grouping.append((row, piece["colNum"]))  # adds the piece to the ally count grouping
                already_checked.add((row, piece["colNum"]))  # adds the piece to the set of already checked pieces
                neighbours_to_check.add((row, piece["colNum"]))

                # checks the all neighbours of the piece, and neighbours of neighbours of neighbours...etc
                valid_neighbours = True
                while valid_neighbours:
                    piece_to_check = neighbours_to_check.pop()
                    adjacent_pieces = get_adj_spaces_in_internal_notation(piece_to_check[0], piece_to_check[1])  # gets adjacent pieces

                    for adjacent_piece in adjacent_pieces:
                        try:
                            if board[adjacent_piece[0]][adjacent_piece[1]]["turn_color"] == turn_color and adjacent_piece not in already_checked:

                                ally_count_grouping.append(adjacent_piece)
                                already_checked.add(adjacent_piece)
                                neighbours_to_check.add(adjacent_piece)

                        except IndexError:
                            pass

                    if len(neighbours_to_check) == 0:
                        ally_count.append(ally_count_grouping)  # adds the grouping to the ally count
                        valid_neighbours = False

                ally_count_grouping = []  # resets the list containing the current ally count grouping

    return ally_count


def get_adj_spaces_in_internal_notation(row, col: int) -> set:
    """
    Gets all the game spaces adjacent to the selected game piece.
    :param row: an int, the number of the row
    :param col: an int, the number of the column
    :param num_pieces_selected: an int, the number of currently selected game pieces
    :return: a set, of the adjacent game spaces
    """
    directions = [
        "NE",
        "E",
        "SE",
        "SW",
        "W",
        "NW"
    ]
    move_directions = {
        "NE": (-1, 1),
        "E": (0, 1),
        "SE": (1, 1),
        "SW": (1, -1),
        "W": (0, -1),
        "NW": (-1, -1)
    }
    adjacent_spaces = set()

    # if the row key is passed, then it is converted to the row number
    if type(row) != int:
        row = Converter.convert_row_to_string_or_int(row)

    # iterates through all possible directions around a given game piece
    for dir in directions:
        # gets the direction coordinate tuple, and gets the adjusted direction tuple
        direction_tuple = move_directions[dir]
        adjusted_direction_tuple = Converter.calculate_adjusted_direction_tuple(row, direction_tuple)

        # gets the internal notation of the adjacent piece
        adjacent_space_internal = Converter.simulate_game_piece_movement(row, col, adjusted_direction_tuple)

        if is_in_bounds(adjacent_space_internal[0], adjacent_space_internal[1]):
            adjacent_spaces.add(adjacent_space_internal)

    return adjacent_spaces


def is_in_bounds(row, col: int) -> bool:
    """
    Checks if the given coordinates is within the game board
    :param row: an int or string, of the row
    :param col: an int, of the colujn
    :return: a boolean, if the coordinates are within the game board
    """
    NUM_COLS_PER_ROW = [
        5,
        6,
        7,
        8,
        9,
        8,
        7,
        6,
        5
    ]
    VALID_ROWS_COLS = range(0, 9)

    if type(row) != int:
        row = Converter.convert_row_to_string_or_int(row)

    if row in VALID_ROWS_COLS and col in VALID_ROWS_COLS:

        COLS_PER_ROW = NUM_COLS_PER_ROW[row]  # gets num of columns for the given row
        if col in range(0, COLS_PER_ROW):  # checks if the column is in bounds for that row
            return True
    else:
        return False


def space_translation(board, adj_list, color):
    """
    finds any same turn_color adjacent pieces to the current piece
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
                if item['turn_color'] == color:
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


# color = "black"
# ally_count = groups(test_board, color)
# print(ally_count)
