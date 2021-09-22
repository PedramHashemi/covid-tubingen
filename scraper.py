import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def scraper():
    numbers = {
        'keine': '0',
        'eins': '1',
        'einen': '1',
        'zwei': '2',
        'drei': '3',
        'vier': '4',
        'fünf': '5',
        'sechs': '6',
        'sieben': '7',
        'acht': '8',
        'neun': '9',
        'zehn': '10',
        'elf': '11',
        'zwölf': '12'
    }

    url = 'https://www.medizin.uni-tuebingen.de/de/hinweise-corona-virus/corona-live-ticker'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    times = soup.find_all("ul", class_="list-bullets timeline")
    times = times[0].find_all('li')
    dates = []
    infected = []
    intensive = []
    for i in range(len(times)):
        # for i in range(40):
        print(i)
        li = times[i]
        date = li.find('span').text
        comment = li.text.split()
        dates.append(date)
        if comment[1] == 'versorgt':
            infected_count = comment[5]
            try:
                intensive_count = int(comment[comment.index('davon') + 1])
            except:
                intensive_count = infected_count

            print(infected_count)
            print(intensive_count)
            try:
                infected.append(int(infected_count) if infected_count.isdigit() else int(numbers[infected_count]))
                intensive.append(int(intensive_count) if intensive_count.isdigit() else int(numbers[intensive_count]))
            except:
                infected.append(0)
                intensive.append(0)

    return {'date': dates, 'infected': infected, 'intensive': intensive}
