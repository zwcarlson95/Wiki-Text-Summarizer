import wikiScrape
import summarizer
from wikiSummarize import cleaner


url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

text = wikiScrape.scrape(url)

clean_text = cleaner.clean(text)

summary = summarizer.summarize(clean_text, 0.1)

print(summary)


