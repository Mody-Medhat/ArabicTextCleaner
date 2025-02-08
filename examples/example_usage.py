# examples/example_usage.py

from ArabicTextCleaner import clean_arabic_text

if __name__ == "__main__":
    raw_text = "أَحْمَدٌ، كيفَ حالُهُ؟ 😊 زور https://example.com للحصول على المزيد #تنظيف_النص"
    print("Original text:")
    print(raw_text)
    
    # Clean the text using all steps
    cleaned_text = clean_arabic_text(
        raw_text,
        remove_emojis_flag=True,
        remove_links_flag=True,
        remove_hashtags_flag=True
    )
    print("\nCleaned text (full pipeline):")
    print(cleaned_text)
