def stray(arr):
    fst = min(arr)
    lst = max(arr)
    
    return fst if arr.count(fst)==1 else lst
    #return min(arr, key=arr.count)
