
from tkinter import *
from gui import Application
from collect import CollectEuroleague

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = 610
height = 450

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.title("Euroleague 2017/18")
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(0, 0)

collect = CollectEuroleague()

app = Application(root,collect.clubs)

root.mainloop()

