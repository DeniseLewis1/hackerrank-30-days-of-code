#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps = 0
    
    for i in range(n):
        for j in range(i, n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                swaps += 1
    
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")