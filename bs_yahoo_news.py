import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

filename = "linklist.txt"
with open(filename, mode="wt") as fp:

    # class部分は度々変わる
    news = soup.find(class_="sc-dAWfgX fqjICZ")

    for element in news.find_all("li"):
        topic = element.text
        link = element.find("a").get("href")
        fp.write(topic + ' ' + link + '\n')