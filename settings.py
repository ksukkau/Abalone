from tkinter import *
import tkinter as tk


class Settings(tk.Toplevel):
    """
    Encapsulates the methods required for drawing, initialized, creating, and handling the various settings menu
    and components.
    """

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.title("Settings")
        self.colors = {"Black": 1,
                       "White": 2}
        self.modes = {"Human v Human": 1,
                      "Human v Computer": 2,
                      "Computer v Computer": 3}
        self.configs = {"Standard": 1,
                        "German Daisy": 2,
                        "Belgian Daisy": 3
                        }
        self.color_choice = IntVar()
        self.mode_choice = IntVar()
        self.board_config = IntVar()
        self.turn_value = IntVar()
        self.turn_timer_value = IntVar()
        self.turn_timer_value2 = IntVar()
        self.selections = {}

    def main_window(self):
        """
        Calls helper methods to manage the settings window.
        """
        self.master.deiconify()
        self.destroy()

    def draw_settings(self):
        """
        Calls helper methods to draw the settings menu as well as its components.
        """
        self.player_color()
        self.game_mode()
        self.select_configuration()
        self.set_turn_limit()
        self.set_turn_timer()
        self.submit_button()

    def player_color(self):
        """
        Draws and creates the settings menu portion to allow the player to select which color they would like
        to play as.
        """
        player_color_label = LabelFrame(self, text="Select player color")
        player_color_label.grid(sticky=W, padx=10)

        for (text, color) in self.colors.items():
            Radiobutton(player_color_label, text=text, variable=self.color_choice,
                        value=color).grid(sticky=W, column=1)

    def game_mode(self):
        """
        Draws and creates the settings menu portion allowing the player to select their desired game mode.
        """
        select_game_mode_label = LabelFrame(self, text="Select game mode")
        select_game_mode_label.grid(sticky=W, padx=10)

        for (text, mode) in self.modes.items():
            Radiobutton(select_game_mode_label, text=text, variable=self.mode_choice,
                        value=mode).grid(sticky=W)

    def select_configuration(self):
        """
        Draws and creates the settings menu portion allowing the player to select their desired starting layout.
        """
        select_config_label = LabelFrame(self, text="Select starting configuration")
        select_config_label.grid(sticky=W, padx=10)

        for (text, config) in self.configs.items():
            Radiobutton(select_config_label, text=text, variable=self.board_config,
                        value=config).grid(sticky=W)

    def set_turn_limit(self):
        """
        Draws and creates the settings menu portion allowing the player to specify the maximum number of turns.
        """
        turn_limit_label = Label(self, text="Enter number of turns per player")
        turn_limit_label.grid()

        turns = Entry(self, textvariable=self.turn_value)
        turns.grid()

    def set_turn_timer(self):
        """
        Draws and creates the settings menu portion allowing the player to specify the time limit for the player within
        the player 1 and 2 spot.
        """
        turn_time_limit_label = Label(self, text="Enter maximum time per turn player 1")
        turn_time_limit_label.grid(padx=10)

        time = Entry(self, textvariable=self.turn_timer_value)
        time.grid()

        turn_time_limit_label2 = Label(self, text="Enter maximum time per turn player 2")
        turn_time_limit_label2.grid(padx=10)

        time2 = Entry(self, textvariable=self.turn_timer_value2)
        time2.grid()

    def submit_button(self):
        """
        Draws, creates, and handles the submit button within the settings menu. Calls a helper method to retrieve the
        settings specified by the player.
        """
        submit = Button(self, text="Submit", command=self.get_data)
        submit.grid()

    def get_data(self):
        """
        Retrieves the specified settings by the player and passes the settings to the main program loop.
        """
        self.selections['color'] = self.color_choice.get()
        self.selections["mode"] = self.mode_choice.get()
        self.selections["config"] = self.board_config.get()
        self.selections["turns"] = self.turn_value.get()
        self.selections["time1"] = self.turn_timer_value.get()
        self.selections["time2"] = self.turn_timer_value2.get()
        self.main_window()
