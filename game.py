import math
from settings import *
from tkinter import *
import tkinter as tk


class GameBoard(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Game")
        self.width = 700
        self.height = 500
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.board_width = 500
        self.hexes_per_side = 5
        self.hexes_across = 2 * self.hexes_per_side - 1
        self.hex_size = self.board_width // self.hexes_across
        self.spot_radius = 25 * self.board_width / 550
        self.piece_radius = 26 * self.board_width / 550
        self.selection_radius = 26 * self.board_width / 550
        self.turn_count_black = 0
        self.turn_count_white = 0
        self.turn = "white"
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
        self.settings_selections = {'color': 0, 'mode': 1, 'config': 0, 'turns': 15, 'time1': 30, 'time2': 30}
        self.spot_coords = {}
        self.board_screen_pos = None
        self.game_board = None

    def new_game_window(self):
        self.set_move_counter()
        self.create_controls()

        self.initialize_game_board_array()
        self.setup_board()
        self.draw_game_board()
        self.draw_pieces()

        self.draw_timer_window()
        self.show_timer()
        self.draw_moves_window()
        self.show_moves()

        self.canvas.bind("<Button-1>", self.click_event_listener_engine)  # sets up mouse click event listener
        self.mainloop()

    def click_event_listener_engine(self, event):
        """
        Handles the user's on-screen click, determines if the player has clicked on a game piece and if so highlights
        the selected game piece chartreuse.
        :param event: an Event object containing various data attributes including the x and y coords of the click event
        """
        RANGE = 20
        print(f"Clicked at {event.x}, {event.y}")

        for row in range(self.hexes_across):
            row_key = self.get_row_key(row)
            selected_row = self.game_board.get(row_key)

            for col in range(self.calculate_row_length(row)):
                piece_x_pos = selected_row[col].get("x_pos")
                piece_y_pos = selected_row[col].get("y_pos")

                # ensures clicked area is within the drawn board piece
                if piece_x_pos - RANGE <= event.x <= piece_x_pos + RANGE:

                    # ensures clicked area is within the drawn board piece
                    if piece_y_pos - RANGE <= event.y <= piece_y_pos + RANGE:
                        selected_piece_color = selected_row[col].get("color")

                        # ensures that the piece clicked is a black or white piece, and not an empty spot on the board
                        if selected_piece_color == "white" or selected_piece_color == "black":
                            self.print_selected_piece_coord(row, col)

                            # redraws the original piece color on the selected piece, enables pieces to be "unselected"
                            self.redraw_piece(selected_piece_color, piece_x_pos,
                                              piece_y_pos)

                            # highlights selected piece green and toggles the "selected" dictionary key
                            if not selected_row[col].get("selected"):
                                selected_row[col].update({"selected": True})
                                self.canvas.create_oval(piece_x_pos - self.selection_radius,
                                                        piece_y_pos - self.selection_radius,
                                                        piece_x_pos + self.selection_radius,
                                                        piece_y_pos + self.selection_radius, fill="chartreuse")
                            else:
                                selected_row[col].update({"selected": False})

    def redraw_piece(self, selected_piece_color, piece_x_pos, piece_y_pos):
        """
        Draws the specified color game piece at the specified x and y coordinates.
        :param selected_piece_color: a string, either 'white' or 'black'
        :param piece_x_pos: a float
        :param piece_y_pos: a float
        """
        self.canvas.create_oval(piece_x_pos - self.piece_radius,
                                piece_y_pos - self.piece_radius,
                                piece_x_pos + self.piece_radius,
                                piece_y_pos + self.piece_radius, fill=selected_piece_color)

    def print_selected_piece_coord(self, row, col):
        """
        Translates the coordinates for the selected game piece according to the I-A and 1-9 game board
        coordinate system.
        :param row: an int
        :param col: an int
        """
        ASCII_ALPHABET_OFFSET = 8
        ZERO_INDEX_OFFSET = 1

        TOP_ROW = 0
        UPPER_HALF = range(1, 4 + ZERO_INDEX_OFFSET)

        num_of_cols = self.calculate_row_length(row)

        if row == TOP_ROW:
            col_coord = num_of_cols + col
        elif row in UPPER_HALF:
            col_coord = (num_of_cols - (row * 2)) + col
        else:
            col_coord = col + ZERO_INDEX_OFFSET

        row_coord = chr((ASCII_ALPHABET_OFFSET - row) + 65)

        print(f"Selected piece at: {row_coord}{col_coord}")

    def draw_game_board(self):
        x = self.width // 2
        y = self.height // 2
        r = 500 // 2
        cos60 = math.cos(math.pi / 3)
        sin60 = math.sin(math.pi / 3)
        self.canvas.create_polygon(x - r, y, x - r * cos60, y - r * sin60, x + r * cos60, y - r * sin60,
                                   x + r, y, x + r * cos60, y + r * sin60, x - r * cos60, y + r * sin60,
                                   fill="slate grey")
        self.draw_board_spots(x, y, r, sin60)
        self.canvas.grid(row=2, column=2, rowspan=25)

    def draw_board_spots(self, x, y, r, sin60):
        for row in range(self.hexes_across):
            row_key = self.get_row_key(row)
            spot_y = (y - r * sin60) + (row * self.hex_size * sin60) + (self.hex_size * sin60 / 2)
            row_length = self.calculate_row_length(row)
            start_x = x - (row_length * self.hex_size // 2) + (self.hex_size // 2)
            for col in range(row_length):
                spot_x = start_x + col * self.hex_size
                self.canvas.create_oval(spot_x - self.spot_radius, spot_y - self.spot_radius,
                                        spot_x + self.spot_radius, spot_y + self.spot_radius, fill="light grey")
                if not self.game_board.get(row_key)[col].get(
                        "x_pos"):  # populating 2D array with positions of drawn pieces
                    self.game_board.get(row_key)[col].update({"x_pos": int(spot_x)})
                    self.game_board.get(row_key)[col].update({"y_pos": int(spot_y)})

    def setup_board(self):
        lines_to_fill = 2

        for row in range(lines_to_fill):
            row_key = "row" + str(row)

            for col in range(self.calculate_row_length(row)):
                self.game_board.get(row_key)[col].update({"color": "white"})

                if row == 1:  # populates front 3 white  pieces
                    for nested_col in range(2, 5):
                        self.game_board.get("row2")[nested_col].update({"color": "white"})

        for row in range(7, 9):
            row_key = "row" + str(row)

            if (row - 1) == 6:  # populates front 3 black pieces
                for nested_col in range(2, 5):
                    self.game_board.get("row6")[nested_col].update({"color": "black"})
            for col in range(self.calculate_row_length(row)):
                self.game_board.get(row_key)[col].update({"color": "black"})

    def initialize_game_board_array(self):
        self.game_board = {}

        for col in range(self.hexes_across):
            row_length = self.calculate_row_length(col)
            row_key = "row" + str(col)
            self.game_board.update({row_key: []})

            for row in range(row_length):
                self.game_board.get(row_key).append(
                    {"colNum": row, "color": None, "selected": False, "x_pos": None, "y_pos": None})

    def calculate_row_length(self, i):
        if self.hexes_per_side + i >= self.hexes_across:
            row_length = self.hexes_per_side + (self.hexes_across - i) - 1
        else:
            row_length = self.hexes_per_side + i
        return row_length

    def get_row_key(self, row, offset=0):
        """
        Generates the key used for the game_board dictionary for denoting the rows of the game board. An offset
        may be specified as the index starts at 0, otherwise the offset is default at 0.
        :param row: an int
        :param offset: an int
        :return: a string
        """
        return "row" + str(row + offset)

    def draw_timer_window(self):
        timer_white_label = Label(self, text="White Player")
        self.white_timer_box = Listbox(self, height=25, width=20)
        timer_white_label.grid(row=1, column=3, padx=5, columnspan=2)
        self.white_timer_box.grid(row=2, column=3, rowspan=6, columnspan=1, padx=5)
        timer_black_label = Label(self, text="Black Player")
        self.black_timer_box = Listbox(self, height=25, width=20)
        timer_black_label.grid(row=8, column=3, padx=5, columnspan=2)
        self.black_timer_box.grid(row=9, column=3, rowspan=6, columnspan=1, padx=5)

    def draw_moves_window(self):

        self.white_moves_box = Listbox(self, height=25, width=20)
        self.white_moves_box.grid(row=2, column=4, rowspan=6, columnspan=1, padx=5)
        self.black_moves_box = Listbox(self, height=25, width=20)
        self.black_moves_box.grid(row=9, column=4, rowspan=6, columnspan=1, padx=5)

    def show_timer(self):
        self.black_timer_box.insert(END, f"Total Time: ", "Time for per move: ")
        self.white_timer_box.insert(END, f"Total Time: ", "Time for per move: ")

    def show_moves(self):
        self.white_moves_box.insert(END, "Moves:")
        self.black_moves_box.insert(END, "Moves:")

    def player_info(self):
        self.set_pieces_count()
        player_one = Label(self, text="White")
        player_one.grid(column=1, padx=3)
        player_one_moves_label = Label(self, text=f"Moves\n{self.white_move_count}")
        player_one_moves_label.grid(column=1, padx=3)
        player_one_pieces_label = Label(self, text=f"Pieces\n{self.white_pieces}")
        player_one_pieces_label.grid(column=1, padx=3)

        player_two = Label(self, text="Black")
        player_two.grid(column=1, padx=3)
        player_two_moves_label = Label(self, text=f"Moves\n{self.black_move_count}")
        player_two_moves_label.grid(column=1, padx=3)
        player_two_pieces_label = Label(self, text=f"Pieces\n{self.black_pieces}")
        player_two_pieces_label.grid(column=1, padx=3)

    def set_pieces_count(self):
        if self.white_pieces is None and self.black_pieces is None:
            self.white_pieces = 14
            self.black_pieces = 14

    def set_move_counter(self):
        try:
            self.get_settings_selections()
        except:
            if self.white_move_count is None:
                self.white_move_count = self.settings_selections['turns']
                self.black_move_count = self.settings_selections['turns']
        self.player_info()

    def create_controls(self):
        start = Button(self, text="Start", width=15)
        stop = Button(self, text="Stop", width=15)
        pause = Button(self, text="Pause", width=15)
        reset = Button(self, text="Reset", width=15)
        undo = Button(self, text="Undo Last", width=15)
        settings = Button(self, text="Settings", width=15, command=self.settings_set_up)

        start.grid(column=1, row=8)
        stop.grid(column=1, row=9)
        pause.grid(column=1, row=10)
        reset.grid(column=1, row=11)
        undo.grid(column=1, row=12)
        settings.grid(column=1, row=13)

    def settings_set_up(self):
        self.new_settings_window()
        self.get_settings_selections()

    def new_settings_window(self):
        self.settings = Settings(self)
        self.settings.focus_set()
        self.settings.draw_settings()
        self.wait_window(self.settings)

    def get_settings_selections(self):
        self.settings_selections = self.settings.selections
        print(self.settings_selections)

    def draw_pieces(self):
        for row in range(self.hexes_across):
            row_key = self.get_row_key(row)
            row_length = self.calculate_row_length(row)

            for col in range(row_length):
                piece_x = self.game_board.get(row_key)[col].get(
                    "x_pos")  # x coordinates of the selected piece
                piece_y = self.game_board.get(row_key)[col].get(
                    "y_pos")  # y coordinates of the selected piece

                # Draw pieces
                if self.game_board.get(row_key)[col].get("color") == "white":
                    self.canvas.create_oval(piece_x - self.piece_radius,
                                            piece_y - self.piece_radius, piece_x + self.piece_radius,
                                            piece_y + self.piece_radius, fill="white")
                elif self.game_board.get(row_key)[col].get("color") == "black":
                    self.canvas.create_oval(piece_x - self.piece_radius,
                                            piece_y - self.piece_radius, piece_x + self.piece_radius,
                                            piece_y + self.piece_radius, fill="black")


g = GameBoard()

g.new_game_window()
