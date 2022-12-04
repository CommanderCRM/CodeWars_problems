import re


def count_smileys(arr):
    count = 0
    regex = r"[:;][-~]?[)D]"
    for string in arr:
        if re.search(regex, string):
            count += 1
    return count
