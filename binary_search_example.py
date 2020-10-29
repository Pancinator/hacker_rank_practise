#usage of binary search aproach an recursion


def find_peak_element(arr, left, right):
    mid = (right+left) // 2

    if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == len(arr)-1 or arr[mid + 1] <= mid):
        return mid

    if arr[mid-1] >= arr[mid] and mid-1 >= 0:
        return find_peak_element(arr, left, mid -1)

    return find_peak_element(arr, mid+1, right)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    left = 0
    right = len(arr) - 1
    index = find_peak_element(arr,left, right)
    print(arr[index])