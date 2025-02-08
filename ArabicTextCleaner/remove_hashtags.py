import re

def remove_hashtags(text: str) -> str:
    """
    Remove all hashtags from the text.
    
    Example:
        "هذا مثال على #تنظيف_النص" -> "هذا مثال على "
    """
    return re.sub(r'#\S+', '', text)
