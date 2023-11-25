from bs4 import BeautifulSoup
import requests
import json

header = {
    'user-agent': 'DanikZhemanov'
}
url = 'https://5element.by/products/767763-igrovoy-noutbuk-asus-tuf-gaming-a17-fa706icb-hx065'
request = requests.get(url=url, headers=header)
print(request.status_code)

with open('../html_files/index4.html', 'r', encoding='UTF-8')as f:
    file = f.read()
    key_info = []
    count_info = []
    soup = BeautifulSoup(file, 'lxml')

    info_all = soup.find_all('td')
    for item in range(len(info_all)):
        if item % 2 == 1:
            print(info_all[item].text.strip())
            count_info.append(info_all[item].text.split())
        elif item % 2 == 0:
            print('__________________')
            print(info_all[item].text.strip())
            key_info.append(info_all[item].text.strip())

print(key_info)
print(count_info)
print(len(key_info))
print(len(count_info))
data = []
for i in range(len(key_info)):
    data_set = {
        f'{key_info[i]}' : f'{count_info[i]}'
    }
    data.append(data_set)
with open('../json_files/5element.json', 'w', encoding='UTF-8')as f:
    json.dump(data, f, ensure_ascii=False, indent=4)