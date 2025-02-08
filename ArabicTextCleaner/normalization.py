import re

def normalize_characters(text: str) -> str:
    """
    Normalize Arabic characters by:
      1-standardizing various forms of 'ا',
      2-removing Tatweel.
      3- removing extra spaces.
    
    Examples:
        'أكل' -> 'اكل'
        'ذهــب' -> 'ذهب'
        'مرحبا   كيف حالك؟  ' -> 'مرحبا كيف حالك؟'
    """
    # Normalize different forms of Alef to bare Alef
    text = re.sub(r'[إأآا]', 'ا', text)
    # Remove Tatweel character
    text = text.replace('ـ', '')
    # Remove extra spaces and trim text
    text = ' '.join(text.split())
    return text