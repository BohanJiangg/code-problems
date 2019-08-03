# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:37:10 2019
Leetcode: Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]


Time Complexity: O(mn), iterates through entire board
Space Complexity: O(mn), uses another board to keep track of changes  

@author: bohan

"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        toRet = []
        for row in range(len(board)):
            temp = []
            for col in range(len(board[0])):
                temp.append(0)
            toRet.append(temp)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                neighbors = 0
                
                for i in range(max(0, row-1), min(row+2, len(board))):
                    for j in range(max(0, col-1), min(col+2, len(board[0]))):
                            if board[i][j] == 1:
                                neighbors+=1
                neighbors -= board[row][col]
                
                
                if board[row][col] == 0 and neighbors == 3:
                    toRet[row][col] = 1
                elif board[row][col] == 1:
                    if neighbors == 2 or neighbors == 3:
                        toRet[row][col] = 1
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = toRet[row][col]
    
    
    
    
    
    
    
    
    
    