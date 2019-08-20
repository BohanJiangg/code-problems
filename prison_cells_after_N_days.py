# -*- coding: utf-8 -*-
"""
Created on August 20 2019
Leetcode: Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """


        N -= max(N - 1, 0) / 14 * 14
        for i in xrange(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells


        # Memory Limit Exceeded
        # if N == 0:
        #     return cells

        # toRet = cells[:]

        # for i in range(N):

        #     if cells[1] == 0:
        #         toRet[0] = 0
        #     if cells[len(cells)-2] == 0:
        #         toRet[len(cells)-1] = 0

        #     for i in range(1, len(cells) -1):
        #         if (cells[i-1] ==  0 and cells[i+1] == 0) or (cells[i-1] == 1 and cells[i+1] == 1):
        #             toRet[i] = 1
        #         else:
        #             toRet[i] = 0
            
        #     cells = toRet[:]
        
        # return toRet
        

        