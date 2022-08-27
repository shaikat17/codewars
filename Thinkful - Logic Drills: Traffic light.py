def update_light(current):
    lst = ['green','yellow','red']
    
    return lst[(lst.index(current)+1)%len(lst)]
