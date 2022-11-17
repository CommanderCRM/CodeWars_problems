def wave(people):
    results = []
    for i in range(len(people)):
        if people[i] == ' ':
            continue
        else:
            results.append(people[:i] + people[i].upper() + people[i+1:])
    return results
