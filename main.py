from bs4 import BeautifulSoup
import requests
import csv
import textwrap

with open("Quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    
    for page_num in range(1,10):
        url = f"https://quotes.toscrape.com/page/{page_num}/"
        html_file = requests.get(url).text

        #html_file = requests.get("https://quotes.toscrape.com/").text
        soup = BeautifulSoup(html_file,"lxml")
        quotes = soup.find_all("div" , class_= "quote")

        for quote in quotes:
            title = quote.find("span", class_= "text").get_text()
            wrapped = textwrap.fill(title, width=40)
            author = quote.find("small" ,class_= "author").get_text()

            tags = quote.find_all("a", class_="tag")
            tag_list = [tag.get_text() for tag in tags]

            writer.writerow([wrapped,author,tag_list])
    
