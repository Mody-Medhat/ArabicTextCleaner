# arabic_text_cleaner/diacritics.py
import re

# Define regex for Arabic diacritics (harakat)
DIACRITICS_REGEX = re.compile(r'[\u064B-\u0652\u0670]') ## \u064B-\u065F\u0610-\u061A\u06D8-\u06DC\u06DF-\u06E8\u06EA-\u06ED

def remove_diacritics(text: str) -> str:
    """
    Remove Arabic diacritics (short vowels and related marks) from the text.
    
    Example:
        "مُحَمَّدٌ" -> "محمد"
    """
    return DIACRITICS_REGEX.sub('', text)
