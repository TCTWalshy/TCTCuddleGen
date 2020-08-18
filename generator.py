import requests
import pprint
from bs4 import BeautifulSoup
import random

class Generator:
    def getNames():
        url = "https://www.theconfigteam.co.uk/meet-the-config-team"
        page = requests.get(url)

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

        return names

    def test(names):
        random.shuffle(names);
        groupNumber = 1
        for i in range(0,len(names),4):
            print("Group ", groupNumber, ': ', names[i:i+4])
            groupNumber+=1

    if __name__ == "__main__":
        test(getNames())
        #cuddleCreator(randomizer(getNames()))