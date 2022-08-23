def is_isogram(string):
    letrs = []
    
    for x in string.lower():
        if x in letrs:
            return False
        else:
            letrs.append(x)
    return True
