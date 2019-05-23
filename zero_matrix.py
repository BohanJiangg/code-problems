# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:40:38 2019

CTCI: Problem 1.8 - Zero Matrix
Time Complexity: O(n),
Space Complexity: O(n),  

@author: bohan
"""


def zero_matrix(matrix):
    
    list_zeroes = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                list_zeroes.append([x,y])
    
    print(list_zeroes)
    
    for coord in list_zeroes:
        # Clear all rows
        for x in range(len(matrix)):
            matrix[x][coord[1]] = 0
    
        # Clear all columns
        for y in range(len(matrix[coord[1]])):
            matrix[coord[0]][y] = 0
    
    
    return matrix



if __name__ == "__main__":
    # Size of matrix
    m = 3
    n = 3
    
    matrix = []
    num = 0
    for i in range(1,m+1):
        row = []
        for j in range(1,n+1):
            num+=1
            row.append(num)
        matrix.append(row)
    
    matrix[1][2] = 0        
    
    print(matrix)
    print(zero_matrix(matrix))
