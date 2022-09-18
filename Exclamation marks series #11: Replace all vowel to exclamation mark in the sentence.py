def replace_exclamation(s):
    vwl = 'aeiou'
    rtr_str = ''
    
    for ch in s:
        if ch.lower() in vwl:
            rtr_str += '!'
        else:
            rtr_str += ch
            
    return rtr_str
