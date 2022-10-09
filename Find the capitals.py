def capitals(word):
    return [cnt for cnt, elm in enumerate(word) if elm.isupper()]
