def number(bus_stops):
    pas_in = 0
    pas_out = 0
    
    for arr in bus_stops:
        pas_in += arr[0]
        pas_out += arr[1]
        
    return (pas_in-pas_out)
    #return sum([stop[0] - stop[1] for stop in bus_stops])
