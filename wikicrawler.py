import urllib.request as urllib
from bs4 import BeautifulSoup
import re

opener = urllib.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('https://en.m.wikipedia.org/wiki/List_of_highest-grossing_Nigerian_films')
openUrl = opener.open(url).read()

soup = BeautifulSoup(openUrl, features="html.parser")

for link in soup.find_all('a', attrs={'href': re.compile("^/wiki"), "title": re.compile("^Cinema")}):
    print(link)