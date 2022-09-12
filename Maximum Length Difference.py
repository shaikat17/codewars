def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    
    return max(abs(len(max(a1, key=len))-len(min(a2, key=len))),abs(len(max(a2, key=len))-len(min(a1, key=len))))
