#never use l+r/2 because there is possibility of overflow

def binary_search(arr, element):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if arr[mid] == element:
            return mid

        if element > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    element = int(input())
    arr = list(map(int, input().rstrip().split()))
    index = binary_search(arr, element)
    print(f"this is index: {index}")