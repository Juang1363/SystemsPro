#! /usr/bin/env python3
from typing import List
def binary_search(array: List[int], val: int) -> int:
               #function body
    left, right = 0, len(array) - 2
    while right >= left :
        middle=left + (right-left) // 2 
        if array[middle] == val:
            return middle
        elif array[middle] < val :
            left = middle + 1
        elif array[middle] > val :
            right = middle - 1
    if left >= right :
            return left      

array = [n for n in range(10)]
print(binary_search(array, 3))
print(binary_search(array, 7))
print(binary_search(array, 11))
print(binary_search(array, 20)) 
 #return index-in-array
