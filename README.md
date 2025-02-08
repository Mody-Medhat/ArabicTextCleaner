# ArabicTextCleaner

**ArabicTextCleaner** is a Python library designed to clean Arabic text for NLP applications. It provides various cleaning functions, allowing users to apply specific text preprocessing steps based on their needs.

## Features

- **Diacritics Removal**: Remove Arabic diacritics (tashkeel).
- **Normalization**: Normalize Arabic text (e.g., converting different forms of "Alef" to a single form).
- **Punctuation Removal**: Remove punctuation marks.
- **Emoji Removal**: Remove all emojis from the text.
- **Hashtag Removal**: Remove hashtags from text.
- **Link Removal**: Remove URLs from text.

## Installation

You can install the package using pip:

```bash
pip install ArabicTextCleaner
```

## Usage
- To use the library, import the required modules and apply the functions on Arabic text.
```bash
from ArabicTextCleaner import diacritics, normalization, punctuation, remove_emojis, remove_hashtags, remove_links

text = "مرحبًا 😊! هذا نصٌّ تجريبيٌّ مع بعض #الهاشتاجات وروابط مثل https://example.com"

# Remove diacritics
cleaned_text = diacritics.remove_diacritics(text)

# Normalize text
cleaned_text = normalization.normalize_arabic(cleaned_text)

# Remove punctuation
cleaned_text = punctuation.remove_punctuation(cleaned_text)

# Remove emojis
cleaned_text = remove_emojis.remove_emojis(cleaned_text)

# Remove hashtags
cleaned_text = remove_hashtags.remove_hashtags(cleaned_text)

# Remove links
cleaned_text = remove_links.remove_links(cleaned_text)

print(cleaned_text)
```
## Project Structure
```bash
ArabicTextCleaner/
│── ArabicTextCleaner/
│   │── __init__.py
│   │── diacritics.py
│   │── normalization.py
│   │── punctuation.py
│   │── remove_emojis.py
│   │── remove_hashtags.py
│   │── remove_links.py
│── examples/
│   │── example_usage.py
│── test/
│── setup.py
│── README.md
```
