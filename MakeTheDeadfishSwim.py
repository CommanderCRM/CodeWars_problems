def parse(data):
    value = 0
    letters = [x for x in data]
    r_arr = []
    for letter in letters:
        if letter == 'i':
            value += 1
        elif letter == 'd':
            value -= 1
        elif letter == 's':
            value *= value
        elif letter == 'o':
            r_arr.append(value)
    return r_arr
