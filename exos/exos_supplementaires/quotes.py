from bs4 import BeautifulSoup
import requests
import csv


nombre_pages = int(input("nombre de pages à parcourir : "))
champs = ["citation", "author"]
contenu = []
for i in range(nombre_pages+1):
    r = requests.get("http://quotes.toscrape.com/page/" + str(i))

    soup = BeautifulSoup(r.text, "html.parser")
    div_quotes = soup.find_all("div", class_="quote")
    for div_quote in div_quotes:
        quote = div_quote.find("span", class_="text")
        author = div_quote.find("small", class_="author")
        contenu.append([quote.text, author.text])


with open("quotes.csv", "w", newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=champs)
    for i in range(len(contenu)):
        csvwriter.writerow({"citation": contenu[i][0].replace("′", ""), "author": contenu[i][1]})
