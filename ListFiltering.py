def filter_list(l):
    no_strings = [x for x in l if not isinstance(x, str)]
    return no_strings
