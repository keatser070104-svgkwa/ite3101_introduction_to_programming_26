def digit_sum(n: int) -> int:
    sum = 0
    for x in str(n):
        sum += int(x)
    return sum
