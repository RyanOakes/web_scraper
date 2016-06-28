import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():

    clear()

    html = urlopen("http://oakesphere.com")

    soup = BeautifulSoup(html, "html.parser")

    # print(soup.prettify())

    # Get all links
    # for link in soup.find_all('a'):
    #     print(link.get('href'))

    # Extract all text
    # print(soup.get_text())


if __name__ == '__main__':
    main()
