
from tkinter import *
from PIL import Image,ImageTk
from collect import clubs
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master):

        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.instruction = Label(self, text="Please choose two teams to compare and hit the Compare button.")
        self.instruction.grid(row=0, column=1, pady=20, sticky=W+E)

        self.team1_chance = Text(self, height=1, width=10)
        self.team1_chance.grid(row=0, column=0, sticky=W)
        self.team2_chance = Text(self, height=1, width=10)
        self.team2_chance.grid(row=0, column=2, sticky=E)

        self.nav_frame = Frame(width = 600)
        self.nav_frame.grid(row=1, column=0)

        self.team1_options = StringVar(self)

        choices = set()
        for c in clubs:
            choices.add(c.team_name)

        self.team1_options.set('Team1')

        self.team2_options = StringVar(self)
        self.team2_options.set('Team2')

        self.team1_menu = OptionMenu(self.nav_frame, self.team1_options, *choices)
        self.team1_menu.config(width=20)
        self.team1_menu.grid(row=1, column=0, padx=20, sticky=E+W)

        self.team2_menu = OptionMenu(self.nav_frame, self.team2_options, *choices)
        self.team2_menu.config(width=20)
        self.team2_menu.grid(row=1, column=2, padx=20, sticky=E+W)

        self.button1 = Button(self.nav_frame, text="Compare", command=self.open_compared)
        self.button1.grid(row=1, column=1, padx=20, sticky=E+W)

        self.body_frame = Frame(width = 600)
        self.body_frame.grid(row=2, column=0, pady=20)

        button_list = []
        r = 0
        c = 0
        for i in range(0, 16):

            button_list.append(Button(self.body_frame, command=lambda i=i: self.open_info(i)))

            img = Image.open(clubs[i].team_logo)
            image = ImageTk.PhotoImage(img)
            button_list[i].config(image=image)
            button_list[i].image = image
            button_list[i].grid(row=r, column=c)
            c = c+1
            if (i+1) % 4 == 0:
                r = r+1
                c = 0

    def open_compared(self):

        if self.team1_options.get() == 'Team1' or self.team2_options.get() == 'Team2':

            messagebox.showerror('Error', 'Teams are not selected.')

        else:

            i_1 = self.get_index(self.team1_options.get())
            i_2 = self.get_index(self.team2_options.get())

            pir1 = clubs[i_1].pir
            pir2 = clubs[i_2].pir

            total = float(pir1) + float(pir2)

            chance1 = 100*float(pir1)//total
            chance2 = 100-chance1

            self.team1_chance.delete(1.0, END)
            self.team1_chance.insert(END, str(chance1)+'%')

            self.team2_chance.delete(1.0, END)
            self.team2_chance.insert(END, str(chance2)+'%')

    def open_info(self, index):

        info = Toplevel()
        window_info = Info(info, index)

    def get_index(self,team_name):

        index=0
        for i in range(0, 16):
            if team_name == clubs[i].team_name:
                index = i
                break

        return index


class Info(Frame):

    def __init__(self, master, index):

        Frame.__init__(self, master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width_local = 400
        height_local = 550

        x_local = (screen_width // 2) - (width_local // 2)
        y_local = (screen_height // 2) - (height_local // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width_local, height_local, x_local, y_local))
        self.master.title(clubs[index].team_name)

        master.name_label = Label(master, text=clubs[index].team_name)
        master.name_label.grid(row=0, column=0, pady=20, sticky=E+W)

        master.r_label = Label(master, text='Stats:', justify=LEFT)
        master.r_label.grid(row=1, pady=10)
        master.stats_label = Label(master, text=clubs[index].get_stats(), justify=LEFT)
        master.stats_label.grid(row=2)

        master.r_label = Label(master, text='Roaster:', justify=LEFT)
        master.r_label.grid(row=3, pady=10)
        roaster = clubs[index].get_roaster()
        master.roaster_label = Label(master, text=roaster, justify=LEFT)
        master.roaster_label.grid(row=4, column=0, padx=60)


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
