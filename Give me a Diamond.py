def diamond(n):
    dmd = ""
    if n % 2 == 0 or not str(n).isdigit():
        return None
    centerRow = n//2+1
    for row in range(1, n+1):
        spaces = abs(centerRow-row)
        dmd += " "*spaces + '*'*(n-spaces*2) +'\n'
        
    return dmd
