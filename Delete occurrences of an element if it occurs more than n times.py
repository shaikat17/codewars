def delete_nth(order,max_e):
    temp = {k: 0 for k in order}
    res = []
    for i in order:
        if temp[i] < max_e:
            temp[i] += 1
            res.append(i)
    return res
