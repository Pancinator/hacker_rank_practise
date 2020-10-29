def find_element(arr, element):
    min = 0
    max = len(arr)
    mid = (max + min) // 2
    left_index = 0
    right_index = 0

    while True:
        if arr[mid] == element:
            index = mid
            break
        elif element > arr[mid]:
            min = mid + 1
            mid = (max + min) // 2
        elif element < arr[mid]:
            max = mid - 1
            mid = (max + min) // 2
        return -1

    index1, index2 = index, index

    while True:
        if arr[index1 - 1] == element:
            index1 -= 1
        else:
            left_index = index1
            break

    while True:
        if arr[index2 + 1] == element:
            index2 += 1
        else:
            right_index = index2
            break

    return left_index, right_index

if __name__ == '__main__':
    element = int(input())
    arr = list(map(int, input().rstrip().split()))
    index = find_element(arr, element)
    print(index)