import re
import requests
from bs4 import BeautifulSoup
from newsplease import NewsPlease

response = requests.get(url='https://cbc.ca')
soup = BeautifulSoup(response.content, 'lxml')

links = []
for link in soup.findAll('a', attrs={'href': re.compile('^https://')}):
    links.append(link.get('href'))

# for link in links: print(link)

article = NewsPlease.from_url('https://x.com/cbc')

for a in dir(article): print(a)