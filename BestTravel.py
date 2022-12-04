from itertools import combinations


def choose_best_sum(t, k, ls):
    arr = list(combinations(ls, k))
    arr = [sum(i) for i in arr if sum(i) <= t]
    if len(arr) == 0:
        return None
    return max(arr)
