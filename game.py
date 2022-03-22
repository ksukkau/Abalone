import math
from settings import *
from tkinter import *
import tkinter as tk
from converter import Converter
from move import Move


class GameBoard(tk.Tk):
    """
    Encapsulates the methods related to drawing, initializing, and creating the game board for Abalone.
    """

    def __init__(self):
        super().__init__()

        # default font and color
        self.font = "Montserrat", 15
        self.font_color = "White"

        # default background color
        self.bg = "#303b41"

        self.title("Game")
        self.width = 700
        self.height = 500
        self.canvas = Canvas(self, width=self.width, height=self.height, bg=self.bg, highlightthickness=0)
        self.board_width = 500
        self.hexes_per_side = 5
        self.hexes_across = 2 * self.hexes_per_side - 1
        self.hex_size = self.board_width // self.hexes_across
        self.spot_radius = 25 * self.board_width / 550
        self.piece_radius = 26 * self.board_width / 550
        self.selection_radius = 26 * self.board_width / 550
        self.selection_redraw_radius = 23 * self.board_width / 550
        self.turn_count_black = 0
        self.turn_count_white = 0
        self.turn = "black"  # black always goes first
        self.game_over = False
        self.selected_pieces = {}
        self.last_hex = None
        self.white_timer = 0
        self.black_timer = 0
        self.white_timer = None
        self.black_timer = None
        self.white_timer_box = None
        self.black_timer_box = None
        self.white_moves_box = None
        self.black_moves_box = None
        self.white_move_count = None
        self.black_move_count = None
        self.white_pieces = None
        self.black_pieces = None
        self.settings = None
        self.settings_selections = {'color': 0, 'mode_p1': "Human", 'mode_p2': "Human", 'config': 0, 'turns': 15,
                                    'time1': 30, 'time2': 30}
        self.spot_coords = {}
        self.board_screen_pos = None
        self.game_board = None

        # ----- For self.Move.ent ----- #
        self.Move = Move()  # initializes the self.Move.object
        self.adjacent_spaces = set()
        self.selected_pieces = []
        self.selected_piece_xy_coords = []
        self.num_pieces_selected = 0

    @staticmethod
    def get_row_key(row: int, offset=0) -> str:
        """
        Generates the key used for the game_board dictionary for denoting the rows of the game board. An offset
        may be specified as the index starts at 0, otherwise the offset is default at 0.
        :param row: an int
        :param offset: an int
        :return: a string
        """
        return "row" + str(row + offset)

    @staticmethod
    def print_selected_piece_coord(row, col):
        """
        Translates the coordinates for the selected game piece according to the I-A and 1-9 game board
        coordinate system, and prints it to the terminal.
        :param row: an int
        :param col: an int
        """
        coords = Converter.internal_notation_to_external(row, col)
        row_coord = coords[0]
        col_coord = coords[1]

        print(f"Selected piece at: {row_coord}{col_coord}")

    def click_event_listener_engine(self, event):
        """
        Handles the user's on-screen click event, and determines if the player has clicked on a game piece. If a game
        piece has been clicked, it is highlighted and the selected game piece is colored green.
        :param event: an Event object containing various data attributes including the x and y coords of the click event
        """
        ZERO_INDEX_OFFSET = 1
        RANGE = 20
        print(f"Clicked at {event.x}, {event.y}")

        for row in range(self.hexes_across):
            row_key = self.get_row_key(row)
            selected_row = self.game_board.get(row_key)

            for col in range(Converter.calculate_row_length(row)):
                piece_x_pos = selected_row[col].get("x_pos")
                piece_y_pos = selected_row[col].get("y_pos")

                # ensures clicked area is within the drawn board piece along the x-axis
                if piece_x_pos - RANGE <= event.x <= piece_x_pos + RANGE:

                    # ensures clicked area is within the drawn board piece along the y-axis
                    if piece_y_pos - RANGE <= event.y <= piece_y_pos + RANGE:
                        selected_piece_color = selected_row[col].get("color")

                        # ensures that the turn color can't select the opposing color's pieces for movement
                        if selected_piece_color == self.turn:

                            if selected_row[col]["selected"]:
                                index_of_selected_piece = self.selected_piece_xy_coords.index(
                                    (piece_x_pos, piece_y_pos))

                                # handles logic when 1st selected piece is selected again
                                if index_of_selected_piece == 0:
                                    self.deselect_pieces()  # 0 means all currently selected pieces are deselected
                                    self.adjacent_spaces = set()  # empties the adjacent spaces set

                                # handles logic when 2nd selected piece is selected again
                                elif index_of_selected_piece == 1:
                                    self.deselect_pieces(1)  # 1 here deselects all pieces but the 1st selected piece

                                    # gets the internal coordinates of the selected piece and gets the adjacent spaces to it
                                    first_piece_internal = self.selected_pieces[0]  # gets the 1st selected piece
                                    self.adjacent_spaces = self.Move.get_adj_game_spaces(first_piece_internal[0],
                                                                                         first_piece_internal[1])

                                # handles logic when 3rd selected piece is selected again
                                elif index_of_selected_piece == 2:

                                    # gets the internal coordinates of the 2nd selected piece and gets the adjacent spaces to it
                                    second_piece_internal_coords = self.selected_pieces[
                                        1]  # 2nd selected piece is always index 1 within self.selected_pieces
                                    self.adjacent_spaces = self.Move.get_adj_game_spaces(
                                        second_piece_internal_coords[0], second_piece_internal_coords[1])

                                    # removes coords of 3rd piece from the list and toggles its 'selected' flag
                                    deselected_piece_internal_coords = self.selected_pieces.pop()  # removes the 3rd, selected piece from the list
                                    self.toggle_selected_flag(deselected_piece_internal_coords[0],
                                                              deselected_piece_internal_coords[
                                                                  1])  # toggles selected flag

                                    # gets the x and y coords of the 3rd selected piece and "unselects" it
                                    deselected_piece_xy_coords = self.selected_piece_xy_coords.pop()
                                    self.draw_game_piece(deselected_piece_xy_coords[0], deselected_piece_xy_coords[1],
                                                         self.turn)

                                    # decrements number of pieces selected
                                    self.num_pieces_selected -= 1

                                """ 
                                add additional logic to determine which selected piece has been clicked (get index using self.selected_pieces)
                                    - if 1st selected piece has been clicked, then unselect everything
                                    - if 2nd or 3rd piece has been clicked, deselect everything after it, including itself
                                        - will have to remove it from both self lists and recreate adjacent spaces for latest selected piece
                                """

                            elif self.num_pieces_selected <= 3:
                                piece_clicked = Converter.internal_notation_to_external(row, col)
                                print(f"Selected piece at: {piece_clicked}")  # prints clicked piece

                                # handles logic for the first piece to be selected
                                if self.num_pieces_selected == 0:
                                    self.num_pieces_selected += 1  # increments number of pieces selected to 1

                                    self.adjacent_spaces = self.Move.get_adj_game_spaces(row,
                                                                                         col)  # gets adjacent spaces

                                    self.draw_game_piece_selection(piece_x_pos, piece_y_pos,
                                                                   self.turn)  # draws game piece selection
                                    self.toggle_selected_flag(row_key, col)  # toggles selected flag
                                    self.selected_pieces.append((row_key, col))  # adds selected piece to a list
                                    self.selected_piece_xy_coords.append(
                                        (piece_x_pos, piece_y_pos))  # adds xy coords to list

                                # handles logic for the second piece to be selected
                                if self.num_pieces_selected == 1:
                                    # checks if the second piece clicked is adjacent to the first
                                    if piece_clicked in self.adjacent_spaces:
                                        self.num_pieces_selected += 1  # increments number of pieces selected to 1

                                        self.adjacent_spaces = self.Move.get_adj_game_spaces(row,
                                                                                             col)  # gets adjacent spaces

                                        self.draw_game_piece_selection(piece_x_pos, piece_y_pos,
                                                                       self.turn)  # draws game piece selection
                                        self.toggle_selected_flag(row_key, col)  # toggles selected flag
                                        self.selected_pieces.append((row_key, col))  # adds selected piece to a list
                                        self.selected_piece_xy_coords.append(
                                            (piece_x_pos, piece_y_pos))  # adds xy coords to list

                                # handles logic for the second piece to be selected
                                if self.num_pieces_selected == 2:
                                    # checks if the second piece clicked is adjacent to the first
                                    if piece_clicked in self.adjacent_spaces:
                                        self.num_pieces_selected += 1  # increments number of pieces selected to 1

                                        self.adjacent_spaces = self.Move.get_adj_game_spaces(row,
                                                                                             col)  # gets adjacent spaces

                                        self.draw_game_piece_selection(piece_x_pos, piece_y_pos,
                                                                       self.turn)  # draws game piece selection
                                        self.toggle_selected_flag(row_key, col)  # toggles selected flag
                                        self.selected_pieces.append((row_key, col))  # adds selected piece to a list
                                        self.selected_piece_xy_coords.append(
                                            (piece_x_pos, piece_y_pos))  # adds xy coords to list

                            print("\n--- Debug ---")
                            print(self.adjacent_spaces)
                            print(self.num_pieces_selected)
                            print(self.selected_piece_xy_coords)
                            print(self.selected_pieces)
                            print("-------------\n")

    def deselect_pieces(self, lower_bound=0):
        """
        Unselects all the selected game pieces within the provided range. The lower bound is specified when the second
        selected piece is clicked again to deselect all pieces but the first selected piece.
        :param lower_bound: an int, either 0 by default or 1.
        """
        ZERO_INDEX_OFFSET = 1

        # iterates over the number of selected pieces and de-selects them if the second selected piece is clicked again
        for iteration in range(lower_bound, self.num_pieces_selected):
            # removes coords from piece in the last position of list and toggles its flag
            deselected_piece_internal_coords = self.selected_pieces.pop()  # removes the 3rd, selected piece from the list
            self.toggle_selected_flag(deselected_piece_internal_coords[0],
                                      deselected_piece_internal_coords[1])  # toggles selected flag

            # gets the x and y coords of the last piece in the list and "unselects" it
            deselected_piece_xy_coords = self.selected_piece_xy_coords.pop()
            self.draw_game_piece(deselected_piece_xy_coords[0], deselected_piece_xy_coords[1], self.turn)

            # decrements number of pieces selected
            self.num_pieces_selected -= 1

    def toggle_selected_flag(self, row_key, col_num: int):
        """
        Toggles the "selected" flag for the provided game piece.
        :param row_key: a string, or an int, of the row of the selected piece
        :param col_num: an int, of the column of the selected piece
        """

        # if the row passed is an int, it is converted to a string so it can be used as a key within the game board dict
        if type(row_key) != str:
            row_key = Converter.convert_row_to_string_or_int(row_key)

        selected_piece = self.game_board.get(row_key)[col_num]
        if not selected_piece["selected"]:
            selected_piece["selected"] = True
        else:
            selected_piece["selected"] = False

    def draw_game_piece(self, piece_x_pos: float, piece_y_pos: float, piece_color: str):
        """
        Draws the specified color game piece at the specified x and y coordinates.
        :param piece_x_pos: a float
        :param piece_y_pos: a float
        :param piece_color: a string, either 'white' or 'black'
        """
        self.canvas.create_oval(piece_x_pos - self.piece_radius,
                                piece_y_pos - self.piece_radius,
                                piece_x_pos + self.piece_radius,
                                piece_y_pos + self.piece_radius, fill=piece_color)

    def draw_game_piece_selection(self, piece_x_pos: float, piece_y_pos: float, piece_color: str):
        """
        Draws the green circle on the game piece that the player has clicked on to select for movement.
        :param piece_x_pos: a float
        :param piece_y_pos: a float
        :param piece_color: a string, either 'white' or 'black'
        """
        self.canvas.create_oval(piece_x_pos - self.selection_radius,
                                piece_y_pos - self.selection_radius,
                                piece_x_pos + self.selection_radius,
                                piece_y_pos + self.selection_radius, fill="green")

        self.canvas.create_oval(piece_x_pos - self.selection_redraw_radius,
                                piece_y_pos - self.selection_redraw_radius,
                                piece_x_pos + self.selection_redraw_radius,
                                piece_y_pos + self.selection_redraw_radius,
                                fill=piece_color)

    def draw_game_board(self):
        """
        Draws the hexagonal shape of the board.
        """
        x_pos = self.width // 2
        y_pos = self.height // 2
        radius = 500 // 2
        cos60 = math.cos(math.pi / 3)
        sin60 = math.sin(math.pi / 3)
        self.canvas.create_polygon(x_pos - radius, y_pos, x_pos - radius * cos60, y_pos - radius * sin60, x_pos +
                                   radius * cos60, y_pos - radius * sin60, x_pos + radius, y_pos, x_pos + radius *
                                   cos60, y_pos + radius * sin60, x_pos - radius * cos60, y_pos + radius * sin60,
                                   fill=self.bg)
        self.draw_board_spaces(x_pos, y_pos, radius, sin60)
        self.canvas.grid(row=2, column=2, rowspan=25, columnspan=3)

    def draw_board_spaces(self, x_pos: int, y_pos: int, radius: int, sin60: float):
        """
        Iterates through the game board containing the representation of the game board and draws a circle to represent
        a game board space in the appropriate location.
        :param x_pos: an int
        :param y_pos: an int
        :param radius: an int
        :param sin60: a float
        """
        for row in range(self.hexes_across):
            row_key = self.get_row_key(row)
            spot_y = (y_pos - radius * sin60) + (row * self.hex_size * sin60) + (self.hex_size * sin60 / 2)
            row_length = Converter.calculate_row_length(row)
            start_x = x_pos - (row_length * self.hex_size // 2) + (self.hex_size // 2)
            for col in range(row_length):
                spot_x = start_x + col * self.hex_size
                self.canvas.create_oval(spot_x - self.spot_radius, spot_y - self.spot_radius,
                                        spot_x + self.spot_radius, spot_y + self.spot_radius, fill="slate grey")

                # populates game_board dictionary with coordinates of each game piece based on the specified game layout
                if not self.game_board.get(row_key)[col].get("x_pos"):
                    self.game_board.get(row_key)[col].update({"x_pos": int(spot_x)})
                    self.game_board.get(row_key)[col].update({"y_pos": int(spot_y)})

    def initialize_game_board_pieces(self):
        """
        Iterates through the game_board data structure, retrieves the x and y coordinates of each board space,
        and draws the game piece on the board of appropriate specified color.
        """
        for row in range(self.hexes_across):
            row_key = self.get_row_key(row)
            row_length = Converter.calculate_row_length(row)

            for col in range(row_length):
                piece_color = self.game_board.get(row_key)[col].get("color")
                piece_x = self.game_board.get(row_key)[col].get("x_pos")  # x coordinates of the selected piece
                piece_y = self.game_board.get(row_key)[col].get("y_pos")  # y coordinates of the selected piece

                self.draw_game_piece(piece_x, piece_y, piece_color)

    def initialize_default_layout(self):
        """
        Initializes the game board array representing the game board with the game pieces of each color in the standard,
        default, layout.
        """
        lines_to_fill = 2

        for row in range(lines_to_fill):
            row_key = "row" + str(row)

            for col in range(Converter.calculate_row_length(row)):
                self.game_board.get(row_key)[col].update({"color": "white"})

                if row == 1:  # populates front 3 white pieces
                    for nested_col in range(2, 5):
                        self.game_board.get("row2")[nested_col].update({"color": "white"})

        for row in range(7, 9):
            row_key = "row" + str(row)

            if (row - 1) == 6:  # populates front 3 black pieces
                for nested_col in range(2, 5):
                    self.game_board.get("row6")[nested_col].update({"color": "black"})
            for col in range(Converter.calculate_row_length(row)):
                self.game_board.get(row_key)[col].update({"color": "black"})

    def initialize_german_layout(self):
        """
        Initializes the game board array representing the game board with the game pieces of each color in the German
        daisy layout.
        """
        ZERO_INDEX_OFFSET = 1
        lines_to_fill = 2 + ZERO_INDEX_OFFSET

        # populates top half of the game board (rows I to F)
        for row in range(lines_to_fill):
            row_key = "row" + str(row)

            for col in range(Converter.calculate_row_length(row)):

                if row == 0:  # populates game pieces on the first row (row I)
                    if col in range(0, 1 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on first row (row I)
                        self.game_board[row_key][col].update({"color": "white"})

                    if col in range(3, 4 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on first row (row I)
                        self.game_board[row_key][col].update({"color": "black"})

                if row == 1:  # populates game pieces on the second row (row H)
                    if col in range(0, 2 + ZERO_INDEX_OFFSET):  # populates 3 white pieces on second row (row H)
                        self.game_board[row_key][col].update({"color": "white"})

                    if col in range(3, 5 + ZERO_INDEX_OFFSET):  # populates 3 black pieces on second row (row H)
                        self.game_board[row_key][col].update({"color": "black"})

                if row == 2:  # populates game pieces on the third row (row G)
                    if col in range(1, 2 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on third row (row G)
                        self.game_board[row_key][col].update({"color": "white"})

                    if col in range(4, 5 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on third row (row G)
                        self.game_board[row_key][col].update({"color": "black"})

        # populates lower half of the game board (rows C to D)
        for row in range(6, 8 + ZERO_INDEX_OFFSET):
            row_key = "row" + str(row)

            for col in range(Converter.calculate_row_length(row)):

                if row == 6:  # populates game pieces on the seventh row (row C)
                    if col in range(1, 2 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on seventh row (row C)
                        self.game_board[row_key][col].update({"color": "black"})

                    if col in range(4, 5 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on seventh row (row C)
                        self.game_board[row_key][col].update({"color": "white"})

                if row == 7:  # populates game pieces on the eighth row (row B)
                    if col in range(0, 2 + ZERO_INDEX_OFFSET):  # populates 3 black pieces on eighth row (row B)
                        self.game_board[row_key][col].update({"color": "black"})

                    if col in range(3, 5 + ZERO_INDEX_OFFSET):  # populates 3 white pieces on eighth row (row B)
                        self.game_board[row_key][col].update({"color": "white"})

                if row == 8:  # populates game pieces on the ninth row (row A)
                    if col in range(0, 1 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on ninth row (row A)
                        self.game_board[row_key][col].update({"color": "black"})

                    if col in range(3, 4 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on ninth row (row A)
                        self.game_board[row_key][col].update({"color": "white"})

    def initialize_belgian_layout(self):
        """
        Initializes the game board array representing the game board with the game pieces of each color in the Belgian
        daisy layout.
        """
        ZERO_INDEX_OFFSET = 1
        lines_to_fill = 3 + ZERO_INDEX_OFFSET

        # populates top half of the game board (rows I to F)
        for row in range(1, lines_to_fill):
            row_key = "row" + str(row)

            for col in range(Converter.calculate_row_length(row)):

                if row == 1:  # populates game pieces on the second row (row H)
                    if col in range(0, 1 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on second row (row H)
                        self.game_board[row_key][col].update({"color": "white"})

                    if col in range(4, 5 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on second row (row H)
                        self.game_board[row_key][col].update({"color": "black"})

                if row == 2:  # populates game pieces on the third row (row G)
                    if col in range(0, 2 + ZERO_INDEX_OFFSET):  # populates 3 white pieces on second row (row HG)
                        self.game_board[row_key][col].update({"color": "white"})

                    if col in range(4, 6 + ZERO_INDEX_OFFSET):  # populates 3 black pieces on second row (row G)
                        self.game_board[row_key][col].update({"color": "black"})

                if row == 3:  # populates game pieces on the fourth row (row F)
                    if col in range(1, 2 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on second row (row F)
                        self.game_board[row_key][col].update({"color": "white"})

                    if col in range(5, 6 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on second row (row F)
                        self.game_board[row_key][col].update({"color": "black"})

        # populates lower half of the game board (rows C to D)
        for row in range(5, 7 + ZERO_INDEX_OFFSET):
            row_key = "row" + str(row)

            for col in range(Converter.calculate_row_length(row)):

                if row == 5:  # populates game pieces on the sixth row (row D)
                    if col in range(1, 2 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on second row (row D)
                        self.game_board[row_key][col].update({"color": "black"})

                    if col in range(5, 6 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on second row (row D)
                        self.game_board[row_key][col].update({"color": "white"})

                if row == 6:  # populates game pieces on the seventh row (row C)
                    if col in range(0, 2 + ZERO_INDEX_OFFSET):  # populates 3 black pieces on second row (row C)
                        self.game_board[row_key][col].update({"color": "black"})

                    if col in range(4, 6 + ZERO_INDEX_OFFSET):  # populates 3 white pieces on second row (row C)
                        self.game_board[row_key][col].update({"color": "white"})

                if row == 7:  # populates game pieces on the eighth row (row B)
                    if col in range(0, 1 + ZERO_INDEX_OFFSET):  # populates 2 black pieces on second row (row B)
                        self.game_board[row_key][col].update({"color": "black"})

                    if col in range(4, 5 + ZERO_INDEX_OFFSET):  # populates 2 white pieces on second row (row B)
                        self.game_board[row_key][col].update({"color": "white"})

    def initialize_game_board_array(self):
        """
        Initializes the dictionary representing the game board containing arrays of dictionaries that contain the
        various attributes of the game pieces. These attributes are: the column number, piece color, if the piece
        has been clicked on by the player, and the piece's x and y coordinates.
        """
        self.game_board = {}

        for col in range(self.hexes_across):
            row_length = Converter.calculate_row_length(col)
            row_key = "row" + str(col)
            self.game_board.update({row_key: []})

            for row in range(row_length):
                self.game_board.get(row_key).append(
                    {"colNum": row, "color": None, "selected": False, "x_pos": None, "y_pos": None})

    def apply_draw_game_board_layout(self):
        self.initialize_game_board_array()

        game_layout = self.settings_selections["config"]
        if game_layout == 2:
            self.initialize_german_layout()
        elif game_layout == 3:
            self.initialize_belgian_layout()
        else:
            self.initialize_default_layout()

        self.draw_game_board()
        self.initialize_game_board_pieces()

    def draw_timer_window(self):
        """
        Initializes and draws the window containing the turn timer for both the black and white team.
        """
        timer_white_label = Label(self, text="White Player", bg=self.bg, font=self.font, fg=self.font_color)
        self.white_timer_box = Listbox(self, height=25, width=20)
        timer_white_label.grid(row=1, column=5, padx=5, columnspan=2)
        self.white_timer_box.grid(row=2, column=5, rowspan=6, columnspan=1, padx=5, pady=5)
        timer_black_label = Label(self, text="Black Player", bg=self.bg, font=self.font, fg=self.font_color)
        self.black_timer_box = Listbox(self, height=25, width=20)
        timer_black_label.grid(row=8, column=5, padx=5, columnspan=2)
        self.black_timer_box.grid(row=9, column=5, rowspan=6, columnspan=1, padx=5, pady=5)

    def draw_moves_window(self):
        """
        Initializes the window used to display the move count of both the black and white team.
        """
        self.white_moves_box = Listbox(self, height=25, width=20)
        self.white_moves_box.grid(row=2, column=6, rowspan=6, columnspan=1, padx=5, pady=5)
        self.black_moves_box = Listbox(self, height=25, width=20)
        self.black_moves_box.grid(row=9, column=6, rowspan=6, columnspan=1, padx=5, pady=5)

    def show_timer(self):
        """
        Initializes the data attribute variable to display the total time and time per move for both the black and white
        teams.
        """
        self.black_timer_box.insert(END, f"Total Time: ", "Time for per move: ")
        self.white_timer_box.insert(END, f"Total Time: ", "Time for per move: ")

    def show_moves(self):
        """
        Initializes the move history window within the GUI for both black and white teams.
        """
        self.white_moves_box.insert(END, "self.Move.:")
        self.black_moves_box.insert(END, "self.Move.:")

    def player_info(self):
        """
        Initializes and draws the statistics for both players, and includes the move and piece count.
        """
        font = ("Montserrat", 18, "bold")
        self.set_pieces_count()
        player_one = Label(self, text="White", bg=self.bg, font=font, fg=self.font_color)
        player_one.grid(column=2, padx=3, row=1)
        player_one_moves_label = Label(self, text=f"self.Move.\n{self.white_move_count}", bg=self.bg, font=self.font,
                                       fg=self.font_color)
        player_one_moves_label.grid(column=2, row=2)
        player_one_pieces_label = Label(self, text=f"Pieces lost\n{self.white_pieces}", bg=self.bg, font=self.font,
                                        fg=self.font_color)
        player_one_pieces_label.grid(column=2, row=3)

        self.current_move_timer()

        player_two = Label(self, text="Black", bg=self.bg, font=font, fg=self.font_color)
        player_two.grid(column=4, padx=3, row=1)
        player_two_moves_label = Label(self, text=f"self.Move.\n{self.black_move_count}", bg=self.bg, font=self.font,
                                       fg=self.font_color)
        player_two_moves_label.grid(column=4, row=2)
        player_two_pieces_label = Label(self, text=f"Pieces lost\n{self.black_pieces}", bg=self.bg, font=self.font,
                                        fg=self.font_color)
        player_two_pieces_label.grid(column=4, row=3)

    def current_move_timer(self):
        font = ("Montserrat", 18, "bold")
        current_move_timer = Label(self, text=f"Time:\n3:00", bg=self.bg, font=font,
                                   fg=self.font_color)
        current_move_timer.grid(column=3, row=2)

    def set_pieces_count(self):
        """
        Initializes the white and black game piece count if it hasn't been initialized.
        """
        if self.white_pieces is None and self.black_pieces is None:
            self.white_pieces = 14
            self.black_pieces = 14

    def set_move_counter(self):
        """
        Initializes the turn and game piece counter within the GUI, and draws it to the window.
        """
        try:
            self.get_settings_selections()
        except:
            if self.white_move_count is None:
                self.white_move_count = self.settings_selections['turns']
                self.black_move_count = self.settings_selections['turns']
        self.player_info()

    def create_controls(self):
        """
        Initializes and draws the buttons within the GUI.
        """
        font2 = "Montserrat", 10
        frame = Frame(self, bg=self.bg)
        start = Button(frame, text="Start", width=10, bg=self.bg, font=font2, fg=self.font_color)
        stop = Button(frame, text="Stop", width=10, bg=self.bg, font=font2, fg=self.font_color)
        pause = Button(frame, text="Pause", width=10, bg=self.bg, font=font2, fg=self.font_color)
        reset = Button(frame, text="Reset", width=10, bg=self.bg, font=font2, fg=self.font_color)
        undo = Button(frame, text="Undo Last", width=10, bg=self.bg, font=font2, fg=self.font_color)
        settings = Button(frame, text="Settings", width=10, bg=self.bg, font=font2, fg=self.font_color,
                          command=self.settings_set_up)

        frame.grid(row=13, columnspan=5, sticky=W, padx=30)
        start.grid(row=13, column=2, padx=3)
        stop.grid(row=13, column=3, padx=3)
        pause.grid(row=13, column=4, padx=3)
        reset.grid(row=13, column=5, padx=3)
        undo.grid(row=13, column=6, padx=3)
        settings.grid(row=13, column=7, padx=3)

    def settings_set_up(self):
        """
        Calls the required helper methods to initialize the settings menu.
        """
        self.new_settings_window()
        self.get_settings_selections()

    def new_settings_window(self):
        """
        Calls the required helper methods to draw the settings window when the user clicks the 'Settings' buttons.
        """
        self.settings = Settings(self)
        self.settings.focus_set()
        self.settings.draw_settings()
        self.wait_window(self.settings)

    def get_settings_selections(self):
        """
        Retrieves the specified settings that the user has selected and prints it to the terminal.
        """
        self.settings_selections = self.settings.selections
        print(self.settings_selections)

        self.apply_draw_game_board_layout()

    def new_game_window(self):
        """
        Performs the method calls for running the Abalone game.
        """
        self.configure(bg=self.bg)
        self.set_move_counter()
        self.create_controls()

        self.apply_draw_game_board_layout()

        self.draw_timer_window()
        self.show_timer()
        self.draw_moves_window()
        self.show_moves()

        self.canvas.bind("<Button-1>", self.click_event_listener_engine)  # sets up mouse click event listener
        self.mainloop()


def main():
    """
    Main function for the Abalone game that acts as an entry point to run the game.
    """
    g = GameBoard()
    g.new_game_window()


if __name__ == '__main__':
    main()
