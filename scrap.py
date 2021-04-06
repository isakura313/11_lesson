import os
import re

import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.combook.ru/tag/Python/p3/")
data = data.text
soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())
name_folder = input("введите название папки ")
os.mkdir(name_folder)

images = soup.find_all('img', src=re.compile(r'\/\w+\/\d{2,10}.jpg'))
print(images)
# images = soup.find_all('href', re.compile(r'\/\w+\/\d{2,10}.jpg'))
for i in range(len(images)):
    data = f'https://www.combook.ru/{images[i]["src"]}'
    print(data)
    data = requests.get(data)
    with open(f'{name_folder}/{str(i)}.jpg', 'wb') as f:
        f.write(data.content)
