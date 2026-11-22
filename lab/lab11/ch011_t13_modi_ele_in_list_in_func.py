n = [3, 5, 7]

for i in range(0, len(n)):
    n[i] = n[i] * 2
# Don't forget to return your new list!


def double_list(l: list) -> list:
    for i in range(0, len(l)):
        l[i] = l[i] * 2
    return l


print(double_list(n))
