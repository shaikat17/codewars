def gimme(input_array):
    srt_arr = sorted(input_array)
    mdl_e = srt_arr[len(srt_arr)//2]
    
    return input_array.index(mdl_e)
    
