def ternary_search(arr, target):
    def search(low, high, target):
        if low > high:
            return -1
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            return search(low, mid1 - 1, target)
        elif target > arr[mid2]:
            return search(mid2 + 1, high, target)
        else:
            return search(mid1 + 1, mid2 - 1, target)
    return search(0, len(arr) - 1, target)
