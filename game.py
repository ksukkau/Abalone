from tkinter import *
import settings

root = Tk()
root.geometry("500x500")
root.title("Game")

submit = Button(root, text="Settings", command=settings.new_settings_window)
submit.grid(pady=10)

root.mainloop()
