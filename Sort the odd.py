def sort_array(source_array):
    odd = [x for x in source_array if x%2!=0]
    odd.sort()
    
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd.pop(0)
    
    return source_array
