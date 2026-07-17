def reverse_list(items):
    reversed = []

    for i in range(len(items)-1, -1, -1):
        reversed.append(items[i])
    
    return reversed
