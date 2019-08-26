# -*- coding: utf-8 -*-
"""
Created on August 26 2019
Leetcode: Battleships in a Board

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


Time Complexity O(m*n), size of matrix
Space Complexity: O(1), store cnt 
@author: bohan
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        if not board:
            return 0

        # DFS through board
        
        def dfs(row, col):
            board[row][col] = '.'
            if row + 1 < len(board) and board[row+1][col] == 'X':
                dfs(row+1,col)
            elif col + 1<len(board[0]) and board[row][col+1] == 'X':
                dfs(row, col+1)
        
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    cnt+=1
                    dfs(i,j)
        
        return cnt
