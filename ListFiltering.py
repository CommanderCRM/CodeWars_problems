def filter_list(l):
    'return a new list with the strings filtered out'
    no_strings = [x for x in l if not isinstance(x, str)]
    return no_strings
