def binary_search(number, target):
    low = numbers[0]
    high = len(numbers) - 1
    mid = low + high // 2
    while low <= high:
        if target == numbers[mid]:
            return numbers[mid] - 1
        elif target < mid:
            high = mid
        elif target > mid:
            low = mid
    if target > high or target < low:
        return -1


numbers = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(numbers, 4))