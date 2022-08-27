import re

def get_count(sentence):
    return len(re.findall('[aeiou]',sentence))
    
#     Using map
#     return sum(map(sentence.count, '[aeiou]'))
