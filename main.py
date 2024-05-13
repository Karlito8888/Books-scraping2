import re

import requests
from bs4 import BeautifulSoup

def main() -> list[int]:
    
    book_ids = []
    
    try:
        response = requests.get("https://books.toscrape.com/index.html")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Il y a eu un problème lors de l'accès au site: {e}")
        raise requests.exceptions.RequestException from e
    
    soup = BeautifulSoup(response.text, "html.parser")
    one_star_books = soup.select("p.star-rating.One")
    # print(f"Il y a {len(one_star_books)} livres à 1 étoile")
    for book in one_star_books:
        try:
            book_link = book.find_next("h3").find("a")["href"]
        except AttributeError as e:
            print(f"Il y a eu un problème lors de la récupération du '<h3>' ")
            raise AttributeError from e
        except TypeError as e:
            print(f"Il y a eu un problème lors de la récupération du '<a>' ")
            raise TypeError from e
        except KeyError as e:
            print(f"Il y a eu un problème lors de la récupération du 'href' ")
            raise KeyError from e
        
        print(f"Le livre {book_link} est à 1 étoile")
        
        try:
            book_id = re.findall(r"_\d{1,}", book_link)[0][1:]
            print(book_id)
        except IndexError as e:
            print(f"Il y a eu un problème lors de la récupération de l'id du livre")
            raise IndexError from e
        else:
            book_ids.append(int(book_id))
            
    return book_ids
        
if __name__ == '__main__':
    print(main())