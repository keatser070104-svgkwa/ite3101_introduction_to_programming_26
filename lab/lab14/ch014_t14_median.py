def median(lst):
    sorted_nums = sorted(lst)
    length = len(sorted_nums)
    mid_index = length // 2
    if length % 2 == 1:
        return sorted_nums[mid_index]
    else:
        return (sorted_nums[mid_index - 1] + sorted_nums[mid_index]) / 2.0
