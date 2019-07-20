# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:34:20 2019
Leetcode: Robot Return to Origin

There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Time Complexity O(n), iterate through array once
Space Complexity: O(1), keep track of 2 variables
@author: bohan
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        if not moves:
            return True
        
        if len(moves) % 2 == 1:
            return False
        
        verti = 0
        hori = 0
        for ch in moves:
            if ch == 'U':
                verti+=1
            elif ch == 'D':
                verti -=1
            elif ch == 'L':
                hori += 1
            elif ch == 'R':
                hori -= 1
        
        if hori == 0 and verti == 0:
            return True
        return False
        
            
            
            
            
            
            
        