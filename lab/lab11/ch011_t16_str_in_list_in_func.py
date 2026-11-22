n = ["Michael", "Lieberman"]
# Add your function here


def join_strings(l: list) -> str:
    s = ""
    for x in l:
        s += x
    return s


print(join_strings(n))
