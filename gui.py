
from tkinter import *
from PIL import Image,ImageTk


class Application(Frame):

    club_selected = 0
    clubs = []

    def __init__(self,master,collectedclubs):

        self.clubs = collectedclubs
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        Team1Options = StringVar(self)

        choices = set()
        for c in self.clubs:
            choices.add(c.teamName)

        Team1Options.set('Team1')

        Team2Options = StringVar(self)
        Team2Options.set('Team2')

        self.instruction = Label(self, text="Please choose two teams to compare and hit the Compare button.")
        self.instruction.grid(row = 0, column = 0, pady = 20, sticky= W+E)

        self.NavFrame = Frame(width = 600)
        self.NavFrame.grid(row = 1,  column = 0)

        self.NavFrame.Team1menu = OptionMenu(self.NavFrame, Team1Options, *choices)
        self.NavFrame.Team1menu.config(width=20)
        self.NavFrame.Team1menu.grid(row = 1, column = 0, padx = 20, sticky = E+W)

        self.NavFrame.Team2menu = OptionMenu(self.NavFrame, Team2Options, *choices)
        self.NavFrame.Team2menu.config(width=20)
        self.NavFrame.Team2menu.grid(row = 1, column = 2, padx = 20, sticky = E+W)

        self.NavFrame.button1 = Button(self.NavFrame, text="Compare", command=lambda :self.open_compared(self.clubs))
        self.NavFrame.button1.grid(row = 1, column = 1, padx = 20, sticky = E+W)

        self.BodyFrame = Frame(width = 600)
        self.BodyFrame.grid(row = 2, column = 0, pady = 20)

        ButtonList = []
        r = 0
        c = 0
        for i in range(0,16):

            ButtonList.append(Button(self.BodyFrame, command=lambda i=i: self.open_info(i,self.clubs)))

            img = Image.open(self.clubs[i].teamLogo)
            image = ImageTk.PhotoImage(img)
            ButtonList[i].config(image=image)
            ButtonList[i].image = image
            ButtonList[i].grid(row=r, column=c)
            c = c+1
            if((i+1) % 4 == 0):
                r = r+1
                c = 0


    def open_compared(self,clubs):
        Compared = Toplevel(self.master)
        window_cmp = TeamsCompared(Compared)

    def open_info(self,index,clubs):
        info = Toplevel(self.master)
        window_info = Info(info,index, clubs)


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


    def __init__(self, master, index, clubs):

        Frame.__init__(self, master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width_local = 400
        height_local = 400

        x_local = (screen_width // 2) - (width_local // 2)
        y_local = (screen_height // 2) - (height_local // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width_local, height_local, x_local, y_local))
        self.master.title(clubs[index].teamName)

        roaster = clubs[index].return_roaster()

        self.master.Label = Label(self.master, text=roaster)
        self.master.Label.grid()




