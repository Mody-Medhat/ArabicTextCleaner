# ArabicTextCleaner/__init__.py

from .normalization import normalize_characters
from .diacritics import remove_diacritics
from .punctuation import remove_punctuation

from .remove_emojis import remove_emojis
from .remove_links import remove_links
from .remove_hashtags import remove_hashtags

def clean_arabic_text(text: str,
                      remove_diacritics_flag: bool = True,
                      normalize_flag: bool = True,
                      remove_punct_flag: bool = True,
                      remove_emojis_flag: bool = False,
                      remove_links_flag: bool = False,
                      remove_hashtags_flag: bool = False) -> str:
    """
    Clean Arabic text by applying a series of cleaning functions.
    
    The cleaning steps include:
      - Normalization of characters
      - Diacritics removal
      - Punctuation removal
      - Optionally, removing emojis, links, and hashtags

    Parameters:
        text (str): The input Arabic text.
        remove_diacritics_flag (bool): If True, remove diacritics.
        normalize_flag (bool): If True, normalize characters.
        remove_punct_flag (bool): If True, remove punctuation.
        remove_emojis_flag (bool): If True, remove emojis.
        remove_links_flag (bool): If True, remove URLs/links.
        remove_hashtags_flag (bool): If True, remove hashtags.

    Returns:
        str: The cleaned text.
    
    """
    if normalize_flag:
        text = normalize_characters(text)
    if remove_diacritics_flag:
        text = remove_diacritics(text)
    if remove_punct_flag:
        text = remove_punctuation(text)
    
    # Apply extra cleaning steps as chosen by the user
    if remove_emojis_flag:
        text = remove_emojis(text)
    if remove_links_flag:
        text = remove_links(text)
    if remove_hashtags_flag:
        text = remove_hashtags(text)
    
    return text
