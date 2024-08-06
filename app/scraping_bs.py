import requests
from bs4 import BeautifulSoup


url = "https://finance.yahoo.com/topic/latest-news/"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')

news = soup.find('div', {"id": "Fin-Stream"}).find('ul', {"class": "My(0) P(0) Wow(bw) Ov(h)"})
news_list = []

for element in news.find_all('li'):
    try:
        title = element.find('h3', {'class': 'Mb(5px)'}).text
        href = element.find('h3', {'class': 'Mb(5px)'}).find('a').get('href')

        news = {
            'title': title,
            'href': href
        }

        news_list.append(news)

    except Exception as e:
        print(f"Error al procesar un artículo: {e}")
        continue

for news in news_list:
    print(news)
