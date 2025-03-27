def sum(a,b):
    return a+b


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1  # Target not found