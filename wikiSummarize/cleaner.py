import re

# removes all references tags from the text
def clean(text):
    clean_text = re.sub(r'\[.*\]', r'', text)
    return clean_text