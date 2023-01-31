def left_join(dictionary1, dictionary2):
    result = []
    for key, value in dictionary1.items():
        if key in dictionary2:
            result.append([key, value, dictionary2.pop(key)])
        else:
            result.append([key, value, "NONE"])
    return result
