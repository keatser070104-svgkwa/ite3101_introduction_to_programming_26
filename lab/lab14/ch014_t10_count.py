def count(sequence, item):
    counter = 0
    for element in sequence:
        if element == item:
            counter += 1
    return counter
