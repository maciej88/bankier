from bs4 import BeautifulSoup
from requests import get
from datetime import datetime as dt



def get_data():

    now = dt.now()
    link = 'https://www.bankier.pl/gielda/notowania/akcje'
    page = get(link)
    bs = BeautifulSoup(page.content, 'html.parser')
    for actions in bs.find_all('tr'):
        try:
            code = actions.a.string
            value = actions.find('td', class_='colKurs change down') or actions.find('td', class_='colKurs change up') or actions.find('td', class_='colKurs change ')
            for td in actions.find_all('td', class_='colWalor textNowrap'):
                title = td.a['title']
                print(f"skrot: {code}, Nazwa: {title}, wartsc: {value.string}, czas: {now}")
        except AttributeError:
            continue


get_data()
