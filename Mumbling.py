def accum(s):
    s_list = list(s)

    r_list = [(s_list[i]*(i+1)).capitalize() for i in range(len(s))]
    return'-'.join(r_list)
