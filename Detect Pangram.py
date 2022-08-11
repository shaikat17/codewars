def is_pangram(s):
    alpa = "abcdefghijklmnopqrstuvwxyz"
    for x in alpa:
        if x not in s.lower():
            return False
    return True
