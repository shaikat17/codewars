def duplicate_encode(word):
    st = ''
    
    for ch in word.lower():
        if word.lower().count(ch) > 1:
            st += ')'
        else:
            st += '('
            
    return st
