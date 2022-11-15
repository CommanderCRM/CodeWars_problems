def is_pangram(s):
    s = s.lower()
    s = list(s)
    s = [x for x in s if x.isalpha()]
    s = sorted(set(s))
    alphabet = sorted(set('abcdefghijklmnopqrstuvwxyz'))
    if s == alphabet:
        return True
    else:
        return False
