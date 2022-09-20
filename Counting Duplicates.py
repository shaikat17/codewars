def duplicate_count(text):
    text = text.lower()
    st_str = set(text)
    return sum(1 if text.count(ch) > 1 else 0 for ch in st_str)
     
