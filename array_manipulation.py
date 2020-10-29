import operator
from collections import defaultdict


def arrayManipulation(n, queries):
    #create dictionary because list is less appropiate
    array = [0]*(n+2)
    for query in queries:
        start_possition = query[0]
        end_possition = query[1]
        value = query[2]
        array[start_possition] += value
        array[end_possition + 1] -= value
    result = get_max(array)
    return result

def get_max(arr):
    sum = 0
    max = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum >= max:
            max = sum
    return max


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    print(arrayManipulation(n, queries))