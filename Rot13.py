def rot13(message):
    all_char = 'abcdefghijklmnopqrstuvwxyz'
    
    cipher = ''
    
    for x in message:
        if x in all_char:
            cipher += all_char[(all_char.index(x)+13)%26]
        elif x in all_char.upper():
            cipher += all_char.upper()[(all_char.upper().index(x)+13)%26]
        else:
            cipher += x
            
    return cipher
