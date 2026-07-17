def join_strings(strings: list[str]) -> str:
    result = ""

    if len(strings) == 0:
        return result
    
    for i in range(0, len(strings)):
        result += strings[i]

        if not i == len(strings) - 1:
            result += ","
    
    return result
