import re

def remove_emojis(text: str) -> str:
    """
    Remove all emojis from the given text.
    
    Example:
        "مرحبا 😊 كيف الحال؟" -> "مرحبا  كيف الحال؟"
    """
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # Flags (iOS)
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)
