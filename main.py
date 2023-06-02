from bs4 import BeautifulSoup
import csv
import requests

source = requests.get("https://coreyms.com/").text
soup = BeautifulSoup(source, "lxml")

csv_file = open("C:/Users/saran/OneDrive/Desktop/scrapper.csv", "w")
file = csv.writer(csv_file)
file.writerow(["title", "content", "link"])

for article in soup.find_all("article"):
    title = article.a.text
    print(title)

    content = article.find("div", class_="entry-content").p.text
    print(content)


    try:
        link = article.find("iframe", class_="youtube-player")["src"]
        print(link)
    except Exception as e:
        None

    print()

    file.writerow([title, content, link])

csv_file.close()

