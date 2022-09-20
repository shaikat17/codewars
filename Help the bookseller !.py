from collections import defaultdict

def stock_list(listOfArt, listOfCat):
    string = ''
    d = defaultdict(int)
    for book in listOfArt:
        for stock in listOfCat:
            if book.startswith(stock):
                d[stock] += int(book.split(" ")[-1])
            else:
                d[stock] += 0
                
    for key, value in d.items():
        string += f'({key} : {value}) - '
    return string.rstrip(' - ') 
