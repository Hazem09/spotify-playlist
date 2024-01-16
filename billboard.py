from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from urllib.error import HTTPError


def getSongs(date):
    def getPage(url):
        try:
            html = urlopen(url)
        except HTTPError as e:
            return None
        bs = BS(html,'html.parser')
        return bs


    page = getPage(f'https://www.billboard.com/charts/hot-100/{date}/')

    divs=page.find_all('div')

    content=[]
    for div in divs:
        title = div.find('h3',id='title-of-a-story')
        if title is not None:
            title = title.get_text().strip()
            if title != 'Songwriter(s):':
                content.append(title)
    playlist=content[19:119]
    print(f'{len(playlist)} songs were retrieved')
    return playlist