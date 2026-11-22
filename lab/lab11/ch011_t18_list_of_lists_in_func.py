n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here


def flatten(l: list) -> list:
    r = []
    for sub in l:
        for x in sub:
            r.append(x)
    return r


print(flatten(n))
