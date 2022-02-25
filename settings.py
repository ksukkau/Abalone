from tkinter import *


def new_settings_window():
    master = Tk()
    master.title("Settings")

    def get_data():
        get_colors_value()
        get_mode_value()
        get_board_config()
        print_turns_data()
        master.destroy()

    def print_turns_data():
        print(turn_value.get())
        print(turn_timer_value.get())

    def get_colors_value():
        print(c.get())

    def get_mode_value():
        print(m.get())

    def get_board_config():
        print(board_config.get())

    colors = {"Black": 1,
              "White": 2}
    modes = {"Human v Human": 1,
             "Human v Computer": 2,
             "Computer v Computer": 3}
    configs = {"Standard": 1,
               "German Daisy": 2,
               "Belgian Daisy": 3
               }

    # User input variables
    c = IntVar()
    m = IntVar()
    board_config = IntVar()
    turn_value = StringVar()
    turn_timer_value = StringVar()

    player_color_label = LabelFrame(master, text="Select player color")
    player_color_label.grid(sticky=W, padx=10)

    for (text, color) in colors.items():
        Radiobutton(player_color_label, text=text, variable=c,
                    value=color).grid(sticky=W, column=1)

    select_game_mode_label = LabelFrame(master, text="Select game mode")
    select_game_mode_label.grid(sticky=W, padx=10)

    for (text, mode) in modes.items():
        Radiobutton(select_game_mode_label, text=text, variable=m,
                    value=mode).grid(sticky=W)

    select_config_label = LabelFrame(master, text="Select starting configuration")
    select_config_label.grid(sticky=W, padx=10)

    for (text, config) in configs.items():
        Radiobutton(select_config_label, text=text, variable=board_config,
                    value=config).grid(sticky=W)

    turn_limit_label = Label(master, text="Enter number of turns")
    turn_limit_label.grid()

    turns = Entry(master, textvariable=turn_value)
    turns.grid()

    turn_time_limit_label = Label(master, text="Enter maximum time per turn")
    turn_time_limit_label.grid(padx=10)

    time = Entry(master, textvariable=turn_timer_value)
    time.grid()

    submit = Button(master, text="Submit", command=get_data)
    submit.grid(pady=10)

    master.mainloop()
