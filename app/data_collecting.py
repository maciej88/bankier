from bs4 import BeautifulSoup
from requests import get
from datetime import datetime as dt

def get_data():
    now = dt.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    link = 'https://www.bankier.pl/gielda/notowania/akcje'
    page = get(link)
    bs = BeautifulSoup(page.content, 'html.parser')
    for actions in bs.find_all('tr'):
        try:
            shortcut = actions.a.string
            value = actions.find('td', class_='colKurs change down') or actions.find('td', class_='colKurs change up') or actions.find('td', class_='colKurs change ')
            for td in actions.find_all('td', class_='colWalor textNowrap'):
                title = td.a['title']
                print(f"skrot: {shortcut}, Nazwa: {title}, wartsc: {value.string}, czas: {dt_string}")
        except AttributeError:
            continue
    print(f"skrot: {shortcut}, Nazwa: {title}, wartsc: {value.string}, czas: {dt_string}")

get_data()
