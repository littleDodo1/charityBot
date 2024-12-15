from bs4 import BeautifulSoup
import requests


def parsLink():
    sites = set()

    url = 'https://www.mos.ru/city/projects/blago/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    chop_elements = results.find("div", class_="css-asjdhw-Box")
    tag_a = chop_elements.find_all("a")

    for a in tag_a:
        href = "https://www.mos.ru" + a.get("href")
        sites.add(href)
    
    return sites
