import requests
import pprint
from bs4 import BeautifulSoup

class Generator:
    def getNames():
        url = "https://www.theconfigteam.co.uk/meet-the-config-team"
        page = requests.get(url)
        pp = pprint.PrettyPrinter(depth=6)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id="block-system-main")

        rows = results.find_all('span', class_='field-content')

        names = []

        for name in rows:
            nameValue = name.find('a')
            names.append(nameValue.text.strip())

        for name in names:
            if name == '':
                names.remove(name)

        names.append("Issy Metcalf")
        names.append("Scott Squires")

        print(names)
        print(len(names))

    if __name__ == "__main__":
        getNames()