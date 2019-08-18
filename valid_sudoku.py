# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:20:13 2019
Leetcode: Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Time Complexity: O(n^2), iterate through entire board 3 times 
Space Complexity: O(n), keep track of seen numbers in a list 


@author: bohan
"""

'''
[[".",".",".",".",".",".","5",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 ["9","3",".",".","2",".","4",".","."],
 [".",".","7",".",".",".","3",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".","3","4",".",".",".","."],
 [".",".",".",".",".","3",".",".","."],
 [".",".",".",".",".","5","2",".","."]]

'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        if not board:
            return True
        
        valid = '123456789'
        
        for row in board:
            lis = []
            for num in row:
                if num != '.' and num in valid and not num in lis:
                    lis.append(num)
                elif num in lis:
                    return False
        
        for col in range(len(board[0])):
            lis = []
            for row in range(len(board)):
                num = board[row][col]
                if num != '.' and num in valid and not num in lis:
                    lis.append(num)
                elif num in lis:
                    return False
        
        i = j = 0
        while i < (len(board)):
            j=0
            while j < len(board[0]):
                lis = []
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        num = board[a][b]
                        if num != '.' and num in valid and not num in lis:
                            lis.append(num)
                        elif num in lis:
                            return False
                j+=3
            i+=3
        
        return True