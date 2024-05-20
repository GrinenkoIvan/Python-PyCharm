# import csv
# import re
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# # def refined(s):
# #     res = re.sub(r"\D+", "", s)
# #     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["rating"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     # p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     # s = soup.find_all("section", class_="plugin-section")[1]
#     # plugins = s.find_all("article")
#     element = soup.find_all("article")
#     for el in element:
#         try:
#             name = el.find("h3").text
#         except AttributeError:
#             name = ""
#
#         try:
#             url = el.find('h3').find('a')["href"]
#         except AttributeError:
#             url = ""
#             print(name)
#     # for plugin in plugins:
#     #     name = plugin.find("h3").text
#     #     url = plugin.find("h3").find("a").get("href")
#     #     rating = plugin.find("span", class_="rating-count").find("a").text
#     #     r = refined(rating)
#     #     data = {'name': name, "url": url, 'rating': r}
#     #     write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/browser/blocks/"
#     # print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


