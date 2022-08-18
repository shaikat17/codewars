def descending_order(num):
    ls = [x for x in str(num)]
    ls.sort(reverse=True)
    return int(''.join(ls))
