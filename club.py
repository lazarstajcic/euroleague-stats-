

class Club():

    def __init__(self, team_name, team_logo_raw, team_roaster, stats_list):

        self.team_name = team_name
        self.team_logo = team_logo_raw
        self.team_roaster = team_roaster
        self.pts = stats_list[1]
        self.fg2 = stats_list[2]
        self.fg3 = stats_list[3]
        self.ft = stats_list[4]
        self.o_reb = stats_list[5]
        self.d_reb = stats_list[6]
        self.t_reb = stats_list[7]
        self.assists = stats_list[8]
        self.steals = stats_list[9]
        self.to = stats_list[10]
        self.b_fv = stats_list[11]
        self.b_ag = stats_list[12]
        self.fouls_c = stats_list[13]
        self.fouls_r = stats_list[14]
        self.pir = stats_list[15]

    def get_roaster(self):

        roaster = ''
        for player in self.team_roaster:
            roaster += player.__str__() + '\n'
        return roaster

    def get_stats(self):

        return 'PTS: ' + self.pts \
                + '   2FG: ' + self.fg2 \
                + '   3FG: ' + self.fg3 \
                + '   FT: ' + self.ft + '\n' \
                + 'OR: ' + self.o_reb \
                + '   DR: ' + self.d_reb \
                + '   TR: ' + self.t_reb \
                + '   AS: ' + self.assists + '\n' \
                + 'ST: ' + self.steals \
                + '   TO: ' + self.to \
                + '   BFv: ' + self.b_fv \
                + '   BAg: ' + self.b_ag + '\n' \
                + 'FCm: ' + self.fouls_c \
                + '   FRv: ' + self.fouls_r \
                + '   PIR: ' + self.pir


class Player():

    def __init__(self, number, name, position, height):

        self.number = number
        self.name = name
        self.position = position
        self.height = height

    def __str__(self):

        return self.number.ljust(8, '_') + self.name.ljust(25, '_') +\
               self.position.ljust(4, '_') + self.height.ljust(5, '_')


