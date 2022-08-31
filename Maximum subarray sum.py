def max_sequence(arr):
    
    if len(arr) == 0:
        return 0
    curSum = 0
    maxSum = arr[0]
    sz = len(arr)
    
    for i in range(sz):
        curSum += arr[i]
        if curSum<0:
            curSum=0
        if curSum>maxSum:
            maxSum = curSum
        
    return maxSum
