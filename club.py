
class Club():

    def __init__(self,team_name,team_logo,team_roaster):

        self.team_name = team_name
        self.team_logo = team_logo
        self.team_roaster = team_roaster

    def __str__(self):
        roaster = ''
        for player in self.team_roaster:
            roaster += player.__str__() + '\n'
        return roaster


class Player():

    def __init__(self, number, name, position, height):

        self.number = number
        self.name = name
        self.position = position
        self.height = height

    def __str__(self):

        return self.number + ' ' + self.name + ' ' + self.position + ' ' + self.height + ' '