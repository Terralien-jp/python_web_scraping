import requests
from bs4 import BeautifulSoup

url =  "http://tsuchiya128.html.xdomain.jp/sample1.html"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

print(soup.find("title").text)
print(soup.find("h1").text)
for element in soup.find_all("strong"):
    print(element.text)