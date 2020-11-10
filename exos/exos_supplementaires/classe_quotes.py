from bs4 import BeautifulSoup
import requests
import csv

class EcrireCSV:
    def __init__(self, citation, auteur, tags):
        self.citation = citation
        self.auteur = auteur
        self.tags = tags

    def enregistrer(self):
        champs = ["citation", "auteur", "tags"]
        with open("classe_quotes.csv", "a", newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=champs, delimiter='|')
            csvwriter.writerow({"citation": self.citation.replace("′", ""), "auteur": self.auteur, "tags": self.tags})


class LireCSV:
    def __init__(self, fichier):
        self.fichier = fichier

    def lire(self):
        with open(self.fichier, "r", newline='') as filecsv:
            csvreader = csv.reader(filecsv)
            for a in csvreader:
                print(" ".join(a))


class RecupererDonnee:
    def __init__(self):
        pass

    def recuperer(self):
        nombre_pages = int(input("nombre de pages à parcourir : "))
        for i in range(nombre_pages+1):
            r = requests.get("http://quotes.toscrape.com/page/" + str(i))
            soup = BeautifulSoup(r.text, "html.parser")
            div_quotes = soup.find_all("div", class_="quote")
            for div_quote in div_quotes:
                tag_citation = []
                quote = div_quote.find("span", class_="text")
                author = div_quote.find("small", class_="author")
                tags = div_quote.find_all("a", class_="tag")
                for tag in tags:
                    tag_citation.append(tag.text)

                ma_citation = EcrireCSV(quote.text, author.text, tag_citation).enregistrer()

RecupererDonnee().recuperer()
LireCSV("classe_quotes.csv").lire()
