import requests
from bs4 import BeautifulSoup
import pandas as pd

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

book_data = []

for page in range(1, 6):

    URL = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        all_books = soup.find_all("article", class_="product_pod")

        for book in all_books:

            title = book.h3.a["title"]

            price = book.find("p", class_="price_color").text

            rating_text = book.find("p", class_="star-rating")["class"][1]

            rating = rating_map[rating_text]

            book_info = {
                "Title": title,
                "Price": price,
                "Rating": rating
            }

            book_data.append(book_info)

    except Exception as e:
        print(f"Error on page {page}: {e}")

df = pd.DataFrame(book_data)

df.to_csv("books.csv", index=False)

print(f"{len(book_data)} books saved successfully!")