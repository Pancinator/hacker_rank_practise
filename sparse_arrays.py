
import math
import os
import random
import re
import sys
from collections import defaultdict

def matchingStrings(strings, queries):
    string_dict = defaultdict(int)
    results = [0]*len(queries)

    for string in strings:
        string_dict[string] += 1

    for i in range(len(queries)):
        if queries[i] in string_dict.keys():
            results[i] = string_dict[queries[i]]
        else:
            results[i] = 0

    return results

if __name__ == '__main__':
    strings_count = int(input())
    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())
    queries = []

    for i in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print(res)