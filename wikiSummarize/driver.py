import wikiScrape
import summarizer
from wikiSummarize import cleaner

def drive():
    url = input("Enter the url for the Wikipedia page: ")
    per = float(input("Enter how much you would like to condense the text: "))

    text = wikiScrape.scrape(url)

    clean_text = cleaner.clean(text)

    summary = summarizer.summarize(clean_text, per)

    return summary