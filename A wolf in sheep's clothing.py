def warn_the_sheep(queue):
    for i in range(len(queue)-1):
        if queue[i] == 'wolf' and queue[i+1] == 'sheep':
            return f"Oi! Sheep number {len(queue)-(i+1)}! You are about to be eaten by a wolf!" 
        
    return 'Pls go away and stop eating my sheep'
