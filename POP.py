from bs4 import BeautifulSoup
import requests

def parse():
    URL ='https://steampay.com/special'
    HEADERS = {
        'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    response = requests.get(URL, headers= HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('a', class_= 'catalog-item')
    comps = []
    for item in items:
        comps.append({
            'title': item.find('div', class_= 'catalog-item__name').get_text(strip = True),
            'price': item.find('span', calss_= 'ccatalog-item__price-span').get_text(strip = True)
        })

        for comp in comps:
            print(comp['title'])
            print(comp['price'])


parse()