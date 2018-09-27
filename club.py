
class Club():

    def __init__(self,teamName,teamLogo,teamRoaster):

        self.teamName = teamName
        self.teamLogo = teamLogo
        self.teamRoaster = teamRoaster


    def return_roaster(self):
        roaster = ''
        for player in self.teamRoaster:
            roaster += player.return_info() + '\n'
        return roaster



class Player():

    def __init__(self, Number, Name, Position, Height):

        self.Number = Number
        self.Name = Name
        self.Position = Position
        self.Height = Height


    def return_info(self):

        return self.Number + ' ' + self.Name + ' ' + self.Position + ' ' + self.Height + ' '