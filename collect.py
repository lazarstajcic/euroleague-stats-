import requests
from bs4 import BeautifulSoup
from club import Club,Player



class CollectEuroleague():

    clubs = []

    def __init__(self,):

        self.grab_euroleague_info()

    def grab_euroleague_info(self):

        source = requests.get('http://www.euroleague.net/competition/teams?seasoncode=E2017').text
        soup = BeautifulSoup(source,'lxml')
        teams = soup.findAll('div', {"class" : 'item'})

        for team in teams:

            Name = team.find('div', {'class': 'RoasterName'}).a.text

            ImageURL = team.find('div', {'class': 'RoasterImage'}).img['src']
            response = requests.get(ImageURL, stream = True)
            response.raw.decode_content = True
            imgRaw = response.raw

            StatsPom = team.find('div', {'class': 'RoasterName'}).a['href']
            Stats = 'http://www.euroleague.net'+StatsPom

            source1 = requests.get(Stats)
            clubPage = BeautifulSoup(source1.text, 'lxml')

            aside = clubPage.find('div', {'class': 'aside'})
            playersPom = aside.find('table').tbody.findAll('tr')

            players = []

            for row in playersPom:

                num = row.find('td', {'class': 'col-no'}).text.strip()
                name = row.find('td', {'class': 'col-name'}).text.strip()
                pos = row.find('td', {'class': 'col-pos'}).text.strip()
                height = row.find('td', {'class': 'col-height'}).text.strip()

                players.append(Player(num,name,pos,height))

            self.clubs.append(Club(Name, imgRaw, players))












