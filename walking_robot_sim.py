# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:51:07 2019
Leetcode: Walking Robot Simulation

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

    -2: turn left 90 degrees
    -1: turn right 90 degrees
    1 <= x <= 9: move forward x units

Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.


Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Time Complexity: O(n+k), the lengths of commands and obstacles, respectively
Space Complexity: O(k), keep track of obstacles in a set  

@author: bohan

"""

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        
        
        if not commands:
            return 0
        
      
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x =y = di = 0
        obstacleSet = set(map(tuple,obstacles))
        ans = 0
        for command in commands:
            if command == -2:
                di = (di - 1) % 4
            elif command == -1:
                di = (di + 1) % 4
            else:
                for i in range(command):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x+=dx[di]
                        y+=dy[di]
                        ans = max(ans, x*x+ y*y)
        return ans
                
                    
    