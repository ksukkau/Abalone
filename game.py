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
        self.selection_radius = 30 * self.board_width / 550
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
        self.settings = None
        self.settings_selections = {}
        self.spot_coords = {}
        self.board_screen_pos = None
        self.board = None

    def new_game_window(self):
        self.player_info()
        self.create_controls()
        self.draw_game_board()
        self.draw_timer_window()
        self.show_timer()
        self.draw_moves_window()
        self.show_moves()
        self.mainloop()

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
        for i in range(self.hexes_across):
            spot_y = (y - r * sin60) + i * self.hex_size * sin60 + self.hex_size * sin60 / 2
            row_length = self.calculate_row_length(i)
            start_x = x - row_length * self.hex_size // 2 + self.hex_size // 2
            for j in range(row_length):
                spot_x = start_x + j * self.hex_size
                self.canvas.create_oval(spot_x - self.spot_radius, spot_y - self.spot_radius,
                                        spot_x + self.spot_radius, spot_y + self.spot_radius, fill="light grey")
                # if not self.board_screen_pos[i][j]:
                #     self.board_screen_pos[i][j] = (spot_x, spot_y)

    def calculate_row_length(self, i):
        if self.hexes_per_side + i >= self.hexes_across:
            row_length = self.hexes_per_side + (self.hexes_across - i) - 1
        else:
            row_length = self.hexes_per_side + i
        return row_length

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
        white_moves = 1  # needs to be updated by program
        black_moves = 2  # needs to be updated by program
        white_pieces = 14
        black_pieces = 14
        player_one = Label(self, text="White")
        player_one.grid( column=1, padx=3)
        player_one_moves_label = Label(self, text=f"Moves\n{white_moves}")
        player_one_moves_label.grid( column=1, padx=3)
        player_one_pieces_label = Label(self, text=f"Moves\n{white_pieces}")
        player_one_pieces_label.grid( column=1, padx=3)

        player_two = Label(self, text="Black")
        player_two.grid(column=1, padx=3)
        player_two_moves_label = Label(self, text=f"Moves\n{black_moves}")
        player_two_moves_label.grid( column=1, padx=3)
        player_two_pieces_label = Label(self, text=f"Moves\n{black_pieces}")
        player_two_pieces_label.grid( column=1, padx=3)

    def create_controls(self):
        start = Button(self, text="Start", width=15)
        stop = Button(self, text="Stop", width=15)
        pause = Button(self, text="Pause", width=15)
        reset = Button(self, text="Reset", width=15)
        undo = Button(self, text="Undo Last", width=15)
        settings = Button(self, text="Settings", width=15, command=self.new_settings_window)

        start.grid(column=1, row=8)
        stop.grid(column=1, row=9)
        pause.grid(column=1, row=10)
        reset.grid(column=1, row=11)
        undo.grid(column=1, row=12)
        settings.grid(column=1, row=13)

    def new_settings_window(self):
        self.settings = Settings(self)
        self.settings.focus_set()
        if 'normal' == self.settings.state():
            print("running")
        self.settings.draw_settings()
        self.get_settings_selections()  # i dont know why this wont print till the main window is closed, it does get it but only when we close main.

    def get_settings_selections(self):
        # I dont know why this doesnt print the data till the main window is closed
        self.settings_selections = self.settings.get_selections()
        print(self.settings_selections)

    def draw_pieces(self):
        for row in range(self.hexes_across):
            row_length = self.calculate_row_length(row)
            for col in range(row_length):
                (piece_x, piece_y) = self.board_screen_pos[row][col]
                # Highlight selected pieces:
                curr_hex = self.board3AxisCoords[row][col]
                for selected in self.selected_pieces:
                    if selected == curr_hex:
                        self.canvas.create_oval(piece_x - self.selection_radius,
                                                piece_y - self.selection_radius, piece_x + self.selection_radius,
                                                piece_y + self.selection_radius, fill="chartreuse")
                # Draw pieces
                if self.board[row][col] == "white":
                    self.canvas.create_oval(piece_x - self.piece_radius,
                                            piece_y - self.pieceRadius, piece_x + self.piece_radius,
                                            piece_y + self.pieceRadius, fill="white")
                elif self.board[row][col] == "black":
                    self.canvas.create_oval(piece_x - self.piece_radius,
                                            piece_y - self.piece_radius, piece_x + self.piece_radius,
                                            piece_y + self.piece_radius, fill="black")

    def set_up_board(self):
        # white - fill first two lines
        lines_to_fill = 2
        for i in range(lines_to_fill):
            for j in range(self.calculate_row_length(i)):
                self.board[i][j] = "white"
        # white - place front 3 pieces
        self.board[lines_to_fill][self.calculate_row_length(lines_to_fill) // 2 - 1] = "white"
        self.board[lines_to_fill][self.calculate_row_length(lines_to_fill) // 2] = "white"
        self.board[lines_to_fill][self.calculate_row_length(lines_to_fill) // 2 + 1] = "white"
        # black - fill first two lines
        lines_to_fill = 2
        for i in range(lines_to_fill):
            for j in range(self.calculate_row_length(i)):
                self.board[self.hexes_across - 1 - i][j] = "black"
        # black - place front 3 pieces
        black_front_row = self.hexes_across - 1 - lines_to_fill
        self.board[black_front_row][self.calculate_row_length(black_front_row) // 2 - 1] = "black"
        self.board[black_front_row][self.calculate_row_length(black_front_row) // 2] = "black"
        self.board[black_front_row][self.calculate_row_length(black_front_row) // 2 + 1] = "black"


g = GameBoard()

g.new_game_window()
