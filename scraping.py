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

    html = urlopen("http://bit.ly/1Ge96Rw")

    soup = BeautifulSoup(html, "html.parser")

    print(soup.prettify())

# http://pythonscraping.com/exercises/exercise1.html
#http://bit.ly/1Ge96Rw

if __name__ == '__main__':
    main()
