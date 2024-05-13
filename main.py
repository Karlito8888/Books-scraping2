import requests
from bs4 import BeautifulSoup

def main():
    try:
        response = requests.get("https://books.toscrape.com/index.html")
        response.raise_for_status()
    except requests.exceptions.RequestException:
        pass
    
    soup = BeautifulSoup(response.text, "html.parser")
        
if __name__ == '__main__':
    main()