import re
import string

def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from the text, including both standard and Arabic-specific punctuation.
    
    Example:
        "مرحبا، كيف حالك؟" -> "مرحبا كيف حالك"
    """
    # Arabic-specific punctuation characters
    arabic_punctuations = "«»…–،؛؟"
    all_punctuations = string.punctuation + arabic_punctuations
    translator = str.maketrans('', '', all_punctuations)
    return text.translate(translator)
