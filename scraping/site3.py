from bs4 import BeautifulSoup
import requests
import json
import re
import time
data_set = []
#url = request.get('https://scrapingclub.com/exercise/list_basic/').text
url = requests.get('https://scrapingclub.com/exercise/list_basic/').text
site = 'https://scrapingclub.com'
for i in range(1,7):
    time.sleep(0)
    site1 = 'https://scrapingclub.com/exercise/list_basic/?page={i}'
    url = requests.get(site1)
    soup =BeautifulSoup(url.text, 'lxml')

    card_all = soup.find_all('div', class_='w-full rounded border')
    for item in card_all:
        time.sleep(0)
        url_card = site + item.find('a').get('href')
        soup = BeautifulSoup(requests.get(url_card).text, 'lxml')
        card = soup.find('div', class_= 'p-6')
        info_card = card.text.strip().split('\n')

        data = dict(
            title = info_card[0],
            print = info_card[1],
            description = info_card[2]
        )
        print(data)
        data_set.append(data)
        print(data_set)
with open('json_files/data_site3.json', 'w', encoding='UTF-8') as f:
    json.dump(data_set, f, ensure_ascii=False, indent=4)