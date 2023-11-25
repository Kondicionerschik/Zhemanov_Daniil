from bs4 import BeautifulSoup
import requests
import json
import re

url = requests.get('https://scrapingclub.com/exercise/detail_json/').text
#
# with open('html_files/index2.html', 'w', encoding='UTF-8')as f:
#     f.write(url)

def pars(site:str):
    soup = BeautifulSoup(site, 'lxml')
    title = soup.find('h3', class_='card-title')
    data_json = soup.find_all('script')[-1].text
    start_index = data_json.find("{")
    end_index = data_json.rfind("}") + 1
    json_string = data_json[start_index:end_index]
    data_json = json_string[18:299].strip()
    print(data_json)

    json_data = json.loads(json_string)
    print(json_data)


if __name__ == '__main__':
    pars(url)