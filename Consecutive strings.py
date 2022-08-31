def longest_consec(strarr, k):
    if k>len(strarr) or k<0:
        return ""
    sz = len(strarr) - k+1
    d = {}
    r_str = ""
    ln = 0
    for i in range(sz):
        com_str = ''.join(strarr[i:i+k])
        # print(com_str)
        d[com_str] = len(com_str)
        
    for key,value in d.items():
        if value>ln:
            ln=value
            r_str=key
    return r_str
