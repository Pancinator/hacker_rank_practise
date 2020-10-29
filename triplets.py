import math
import os
import random
import re
import sys
from collections import defaultdict


def countTriplets(arr, ration):
    count = 0
    combinations_dict, possible = defaultdict(int), defaultdict(int)

    for a in arr:
        if combinations_dict[a]:
            count += combinations_dict[a]

        if possible[a]:
            combinations_dict[a*ration] += possible[a]
        possible[a*r] += 1
    return count

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans) + '\n')

