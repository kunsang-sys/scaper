import requests
from bs4 import BeautifulSoup 

url = "https://books.toscrape.com/"

def scrape(url):
    responce = requests.get(url)
    print(responce)


scrape(url)

def scrape(url):
    response = requests.get(url)
    if response.status_code != 200:
        return
    
    response.encoding = response.apparent_encoding


    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all("article",class_="product_pod")
    all_books = []
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p",class_='price_color').text
        
        currency = price_text[0]
        price=float(price_text[1:])
        book_info = {
            'title':title,
            'currency':currency,
            'price':price
        }
        all_books.append(book_info)
    

    return all_books

books = scrape(url)


with open("book.json","w") as f:
    import json 
    json.dump(books,f)
        