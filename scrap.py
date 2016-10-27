from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup
import re


def getPage(url):
    """
    get object donor
    :param url: string
    :return: BeautifulSoup objects
    """
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj


def getTable(url):
    """
    get table donor
    :param url:bs4.element.NavigableString'
    :return: table obj BeautifulSoup
    """
    table = getPage(url).tbody
    return table


def getData(url, result):
    """
    Getting data scraping
    :param url: string
    :return: list[dict]
    """
    items = getTable(url).find_all('tr', {'class': ['even', 'odd']})
    for item in items:

        # getting quest id and name
        quest_link = item.find('td', {'class': 'col-t name col-name'}).find('a').get('href')
        quest_name = item.find('td', {'class': 'col-t name col-name'}).find('a').text
        quest_id = re.findall('\d+', quest_link)[0]

        # getting quest req
        quest_req = item.find('td', {'class': ''}).text

        # getting quest level
        quest_level = item.findAll('td', {'class': ''})[1].text
        quest_level = quest_level.strip()

        # getting quest category
        quest_category = item.find('td', {'class': ''}).next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text

        result.append({
            'id': quest_id,
            'name': quest_name,
            'req': quest_req,
            'level': quest_level,
            'category': quest_category
        })
    return result

def getAllLink(url):
    """
    Getting full links for scraping
    :param url: string
    :return: list
    """
    links = []
    domain = 'http://www.wowdb.com'
    link = str()
    step = getPage(url)
    links.append(url)
    while link != '!!':
        try:
            link = step.find('div', {'class': 'b-pagination b-pagination-a'}).find('a', {'rel': 'next'}).get('href')
        except AttributeError:
            link = '!!'

        if link != '!!':
            link = domain + link
            links.append(link)
            step = getPage(link)
        else:
            break

    return links
