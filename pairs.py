
#!/bin/python3
import math
import os
import random
import re
import sys

# problem solved withquadratical complexity
# that is because list is
def pairs(k, arr):
    pairs_count = 0
    for number in arr:
        if arr.count(number + k) == 1:
            pairs_count += 1
    return pairs_count

#with usage of dictionary this alghoritms performs much much better
def pairs2(k, a):
    myDict = {item: 1 for item in a}
    count = 0
    for each in myDict:
        if each + k in myDict:
            count += 1
    return count

if __name__ == '__main__':

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(str(result) + '\n')

