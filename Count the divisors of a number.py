import math

def divisors(n):
    arr = []
    i = 1
    while i <= math.sqrt(n):
          
        if (n % i == 0) :
              
            # If divisors are equal, print only one
            if (n / i == i) :
                arr.append(i)
            else :
                # Otherwise print both
                arr.append(i)
                arr.append(n/i)
        i = i + 1
        
    return len(arr)
