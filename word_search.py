# -*- coding: utf-8 -*-
"""
Created on July 22 2019
Leetcode: Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Time Complexity O(n*m*len(word)), for n = numRows and m = numColumns 
Space Complexity: O(1), need constant number of variables to keep track of visited nodes; modify board in place 
@author: bohan
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            return False
        
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, word):
            if len(word) == 0:
                return True
        
            if row < 0 or row >= rows or col < 0 or col >= cols  or board[row][col] != word[0]:
                return False
            
            temp = board[row][col]
            board[row][col] = '*'
            res = dfs(row+1, col, word[1:]) or dfs(row-1, col, word[1:]) or dfs(row, col-1, word[1:]) or dfs(row, col+1, word[1:])
            board[row][col] = temp
            return res


        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, word):
                    return True
        
        return False