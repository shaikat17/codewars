def is_square(n):
    try:
        return int(n**0.5)**2==n
    except:
        return False
