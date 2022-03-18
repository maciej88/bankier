from bs4 import BeautifulSoup
from requests import get
from datetime import datetime as dt
import sqlite3
import os


def get_data():
    # drop and recreate new database
    os.remove('db.sqlite3')
    with open('db.sqlite3', 'w') as fp:
        pass
    # create new database
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS app_stock (name varchar(64), code varchar(32), price double precision , date TIMESTAMP)''')
    link = 'https://www.bankier.pl/gielda/notowania/akcje'
    now = dt.now()
    page = get(link)
    bs = BeautifulSoup(page.content, 'html.parser')
    for actions in bs.find_all('tr'):
        try:
            code = str(actions.a.string)
            price = actions.find('td', class_='colKurs change down').get_text() or actions.find('td',
                                                                                                class_='colKurs change up').get_text() or actions.find(
                'td', class_='colKurs change ').get_text()
            for td in actions.find_all('td', class_='colWalor textNowrap'):
                name = td.a['title']
                cursor.execute('INSERT OR REPLACE INTO app_stock VALUES (?, ?, ?, ?)', (name, code, price, now))
                db.commit()

        except AttributeError:
            continue
    db.close()


get_data()
