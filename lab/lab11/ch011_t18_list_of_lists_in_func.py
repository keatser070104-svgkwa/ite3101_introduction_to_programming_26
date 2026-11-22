from typing import List


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here


def flatten(lists: List[List[int]]) -> List[int]:
    results = []
    for leve11 in lists:
        for leve12 in leve11:
            results.append(leve12)
    return results
# print(flatten(n))
