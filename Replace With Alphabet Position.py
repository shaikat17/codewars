def alphabet_position(text):
    lst = 'abcdefghijklmnopqrstuvwxyz'
    
    return ' '.join([str(lst.index(x)+1) for x in text.lower() if x in lst])
