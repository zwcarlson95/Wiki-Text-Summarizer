from bs4 import BeautifulSoup
import requests

# scrapes all text from the page
def scrape(url):
    text = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list(soup.children)
    lines = soup.find_all('p') # creates a list containing every individual line of text in the page

    for line in lines:
      text += line.get_text() # adds each line of text to a single string

    return text




