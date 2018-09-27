
from tkinter import *
from PIL import Image,ImageTk
from collect import clubs


class Application(Frame):

    def __init__(self, master):

        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        team1_options = StringVar(self)

        choices = set()
        for c in clubs:
            choices.add(c.team_name)

        team1_options.set('Team1')

        team2_options = StringVar(self)
        team2_options.set('Team2')

        self.instruction = Label(self, text="Please choose two teams to compare and hit the Compare button.")
        self.instruction.grid(row = 0, column = 0, pady = 20, sticky= W+E)

        self.nav_frame = Frame(width = 600)
        self.nav_frame.grid(row = 1,  column = 0)

        self.nav_frame.team1_menu = OptionMenu(self.nav_frame, team1_options, *choices)
        self.nav_frame.team1_menu.config(width=20)
        self.nav_frame.team1_menu.grid(row = 1, column = 0, padx = 20, sticky = E+W)

        self.nav_frame.team2_menu = OptionMenu(self.nav_frame, team2_options, *choices)
        self.nav_frame.team2_menu.config(width=20)
        self.nav_frame.team2_menu.grid(row = 1, column = 2, padx = 20, sticky = E+W)

        self.nav_frame.button1 = Button(self.nav_frame, text="Compare", command=self.open_compared)
        self.nav_frame.button1.grid(row = 1, column = 1, padx = 20, sticky = E+W)

        self.body_frame = Frame(width = 600)
        self.body_frame.grid(row = 2, column = 0, pady = 20)

        button_list = []
        r = 0
        c = 0
        for i in range(0,16):

            button_list.append(Button(self.body_frame, command=lambda i=i: self.open_info(i)))

            img = Image.open(clubs[i].team_logo)
            image = ImageTk.PhotoImage(img)
            button_list[i].config(image=image)
            button_list[i].image = image
            button_list[i].grid(row=r, column=c)
            c = c+1
            if((i+1) % 4 == 0):
                r = r+1
                c = 0

    def open_compared(self):

        compared = Toplevel(self.master)
        window_cmp = TeamsCompared(compared)

    def open_info(self,index):

        info = Toplevel(self.master)
        window_info = Info(info,index)


class TeamsCompared(Frame):

    def __init__(self,master):

        Frame.__init__(self, master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width_local = 400
        height_local = 400

        x_local = (screen_width // 2) - (width_local // 2)
        y_local = (screen_height // 2) - (height_local // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width_local, height_local, x_local, y_local))
        self.master.title("Comparation Engine")


class Info(Frame):

    def __init__(self, master, index):

        Frame.__init__(self, master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width_local = 400
        height_local = 400

        x_local = (screen_width // 2) - (width_local // 2)
        y_local = (screen_height // 2) - (height_local // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width_local, height_local, x_local, y_local))
        self.master.title(clubs[index].team_name)

        roaster = clubs[index].__str__()

        self.master.label = Label(self.master, text=roaster)
        self.master.label.grid()


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

app = Application(root)

root.mainloop()

