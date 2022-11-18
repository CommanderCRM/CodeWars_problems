import collections

def find_it(seq):
    elements_count = collections.Counter(seq)
    for key, value in elements_count.items():
        if value % 2 != 0:
            return key
