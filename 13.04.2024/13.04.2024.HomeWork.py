# import requests
# from bs4 import BeautifulSoup
#
# HOST = 'https://www.chitai-gorod.ru'
# url = 'https://www.chitai-gorod.ru/catalog/books/klassicheskaya-proza-110003'
# HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applicatio',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# }
#
#
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='products-list')
#     cards = []
#
#     for item in items:
#         cards.append(
#             {
#                 'title': item.find('div', class_='product-list').get_text(),
#                 'linc': item.find('div', class_='product-list').find('a').get('href'),
#                 'author': item.find('div', class_='product-list').get_text()
#             }
#         )
#     return cards
#
#
# html = get_html(url)
# print(get_content(html.text))


import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        response = requests.get(self.url).text
        self.html = BeautifulSoup(response, 'lxml')

    def parsing(self):
        news = self.html.find_all('div', class_='caption')
        for item in news:
            title = item.find('h3').text
            href = item.find('h3').find('a').get('href')
            author = item.find('a', class_='topic-info-author-link').text.strip()
            self.res.append({
                'title': title,
                'href': href,
                'author': author
            })

    def save(self):
        with open(self.path, 'w') as file:
            i = 1
            for item in self.res:
                file.write(
                    f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\nАвтор: {item["author"]}'
                    f'\n\n{"*" * 30}\n'
                )
                i += 1

    def run(self):
        for i in range(1, 5):
            self.url + f'page{i}/'
            self.get_html()
            self.parsing()
            self.save()


def main():
    pars = Parser(
        url='https://www.ixbt.com/live/index/news/',
        path='news.txt'
    )
    pars.run()


if __name__ == '__main__':
    main()
