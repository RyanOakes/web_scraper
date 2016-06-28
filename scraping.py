from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://oakesphere.com")

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())
