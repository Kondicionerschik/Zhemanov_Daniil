from bs4 import BeautifulSoup
import requests
import json

url = requests.get('https://scrapingclub.com/exercise/detail_basic/').text
with open('html_files/index1.html', 'w', encoding='UTF-8')as f:
    f.write(url)


def pars(site: str):

    soup = BeautifulSoup(site, 'lxml')
    title = soup.find('h3', class_='card-title').text
    object_price = soup.find('h4', class_='my-4 card-price').text
    decr = soup.find('p', class_='card-description').text.split('.')
    info_obj = decr[1].strip()
    compound_ = decr[-2].strip()
    data_set = dict(
        name = title,
        price = object_price,
        info = info_obj,
        compound = compound_
    )

    with open('json_files/data_site1.json', 'a', encoding='UTF-8')as f:
        json.dump(data_set, f, ensure_ascii=False, indent=4)





if  __name__ == '__main__':
    pars(url)