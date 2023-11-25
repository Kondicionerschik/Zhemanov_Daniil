from bs4 import BeautifulSoup
import requests
import json

url = 'https://smart-lab.ru/blog/735640.php'
request = requests.get(url=url)
print(request.status_code)

with open('../html_files/index5.html', 'r', encoding='UTF-8')as f:
    file = f.read()


def pars(site:str):
    new_list = []
    soup = BeautifulSoup(file, 'lxml')
    text = soup.find('div', class_='topic bluid_50457').find_all('strong')
    for i in text:
        print(i.text.strip('\n'))
        new_list.append(i.text.strip('\n'))
        print(new_list)
        print('----------------------')


if __name__ == '__main__':
    pars(url)