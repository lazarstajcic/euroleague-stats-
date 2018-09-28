import requests
from bs4 import BeautifulSoup
from club import Club, Player


clubs = []

source = requests.get('http://www.euroleague.net/competition/teams?seasoncode=E2017').text
soup = BeautifulSoup(source, 'lxml')
teams = soup.findAll('div', {"class": 'item'})

for team in teams:

    club_name = team.find('div', {'class': 'RoasterName'}).a.text

    image_url = team.find('div', {'class': 'RoasterImage'}).img['src']
    response = requests.get(image_url, stream=True)
    response.raw.decode_content = True
    img_raw = response.raw

    page_pom = team.find('div', {'class': 'RoasterName'}).a['href']
    club_page_url = 'http://www.euroleague.net'+page_pom

    source1 = requests.get(club_page_url)
    club_page = BeautifulSoup(source1.text, 'lxml')

    aside = club_page.find('div', {'class': 'aside'})
    players_pom = aside.find('table').tbody.findAll('tr')

    players = []

    for row in players_pom:

        num = row.find('td', {'class': 'col-no'}).text.strip()
        name = row.find('td', {'class': 'col-name'}).text.strip()
        pos = row.find('td', {'class': 'col-pos'}).text.strip()
        height = row.find('td', {'class': 'col-height'}).text.strip()

        players.append(Player(num, name, pos, height))

    average_team_stats_row = club_page.find('tr', {'class': 'AverageFooter'})
    average_team_stats_list = average_team_stats_row.findAll('span')

    team_stats_list = []

    for stat in average_team_stats_list:

        team_stats_list.append(stat.text)

    clubs.append(Club(club_name, img_raw, players, team_stats_list))
