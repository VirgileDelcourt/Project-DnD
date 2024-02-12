from tkinter import Label
from Scripts.BaseWindow import Window, bg


class CombatWindow(Window):
    def __init__(self, manager, mapmanager):
        super().__init__(manager, "Dumbs and Dungeons")

        self.map = []
        for y in range(10):
            self.map.append([])
            for x in range(10):
                temp = Label(self.window, text="buttno :)", width=10, height=5, bg=bg)
                self.map[-1].append(temp)
                temp.grid(column=x, row=y)
                temp.bind("<Button-1>", lambda _: print("1"))
                temp.bind("<Button-1>", lambda _: print("2"))

        self.mapmanager = mapmanager
        self.update()

    def update(self):
        for y in range(10):
            for x in range(10):
                temp = self.mapmanager.check_occupy((x, y))
                if temp:
                    self.map[y][x].config(text=temp.name, bg="grey")
