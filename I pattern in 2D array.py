#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    


    
def count (arr, start_index):
    start_row = start_index[0]
    start_col = start_index[1]
    
    total = 0
    
    for i in range(3):
        total += arr[start_row][start_col + i]
        total += arr[start_row + 2][start_col + i]
        
    total += arr[start_row + 1][start_col + 1]
    
    return total

max_total = -9 * 9
for i in range(len(arr)-2):
    for j in range (len(arr[i])-2):
        total = count(arr, [i, j])
        if total > max_total:
            max_total = total
            
    
print (max_total)