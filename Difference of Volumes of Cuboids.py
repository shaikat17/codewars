def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


def find_difference(a, b):
    return abs(multiplyList(a)-multiplyList(b))
