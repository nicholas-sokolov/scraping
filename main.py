from scrap import *
import csv


def main():
    url = 'http://www.wowdb.com/quests?filter-expansion=7&filter-cb-race=33555378&filter-cb-class=16'
    links = getAllLink(url)
    data_scrap = []
    for link in links:
        data_scrap = getData(link, data_scrap)
    print(data_scrap)

    with open('result.csv', 'w') as scraping:
        title = ['id', 'name', 'req', 'level', 'category']
        writer = csv.DictWriter(scraping, fieldnames=title)
        writer.writeheader()
        writer.writerows(data_scrap)

if __name__ == '__main__':
    main()
