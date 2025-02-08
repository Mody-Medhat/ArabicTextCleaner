import re

def remove_links(text: str) -> str:
    """
    Remove all links (URLs) from the text.
    
    Example:
        'لمزيد من التفاصيل زور google.com' -> 'لمزيد من التفاصيل زور'
    """
    text = re.sub(r'(http\S+|www\.\S+|[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', '', text)
    return ' '.join(text.split())  