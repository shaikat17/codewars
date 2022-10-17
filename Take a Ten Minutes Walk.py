def is_valid_walk(walk):
    north_south =  walk.count('n') == walk.count('s') 
    east_west =  walk.count('e') == walk.count('w')
    length = len(walk) == 10
    return north_south and east_west and length
