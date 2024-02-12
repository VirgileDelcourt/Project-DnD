from tkinter import Tk

bg = "#f42069"


class Window:
    def __init__(self, manager, name="", size="1080x760"):
        self.window = Tk()
        self.window.title(name)
        self.window.geometry(size)
        self.window.config(bg=bg)

        self.manager = manager  # contains a GameManager

    def run(self):
        self.window.mainloop()

    def end(self):
        self.window.destroy()
