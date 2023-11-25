from bs4 import BeautifulSoup
import requests
site = 'cсылка'
# with open('html...', 'w', encoding='UTF-8') as f:
#     f.write(site.text)


with open('cсылка', 'r', encoding='UTF-8') as f:
    file = r.read()

    soup = BeautifulSoup(file, 'lxml')

    print(soup.find('h1'))