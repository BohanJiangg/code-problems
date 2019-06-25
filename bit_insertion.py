# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:01:09 2019

CTCI: Problem 5.1 - Insertion

Time Complexity: O(n),
Space Complexity: O(n),  

@author: bohan

"""



def insertion(N, M, i, j):
    N = int(str(N), 2)
    M = int(str(M), 2)
    print(N)
    for k in range(i, j+1):
        mask = ~(1<<k)
        
        N = N & mask
    
    print(bin(mask))

if __name__ == "__main__":
    print(insertion(10000000000, 10011, 2, 6))
    print('Correct answer is: {}'.format(int(str('10001001100'),2)))