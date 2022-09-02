def title_case(title, minor_words=''):
    if not len(title):
        return title
    
    r_sen = []
    new_minor_words = [word.lower() for word in minor_words.split(' ')]
    
    for index, word in enumerate(title.split(' ')):
        if index == 0:
            r_sen.append(word.title())
            continue

        if word.lower() in new_minor_words:
            r_sen.append(word.lower())
            continue

        r_sen.append(word.title())
            
    return ' '.join(r_sen)
    
