def nb_dig(n, d):
    values_list = list(range(0, n+1))
    list_squared = [str(x**2) for x in values_list]
    str_list_squared = ''.join(list_squared)
    return str_list_squared.count(str(d))
