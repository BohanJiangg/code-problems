# -*- coding: utf-8 -*-
"""
Created on August 19 2019
Leetcode: Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.


Time Complexity O(n), worse case where large negative asteroid at the end of all positive asteroids 
Space Complexity: O(n), keep track of surviving asteroids  
@author: bohan
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids:
            return None
        
        # Collisions only when negative numbers to the right of positive ones
        
        # Find first positive number
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                break
        
        i+=1
        toRet = asteroids[ :i]
        while i < len(asteroids):
            
            curr = asteroids[i]
            if curr > 0 :
                toRet.append(curr)
            elif not toRet or toRet[-1] < 0:
                toRet.append(curr)
            else:
                # asteroids[i] < 0, will collide
                
                while toRet and toRet[-1] > 0:
                    if toRet[-1] > abs(curr):
                        # this asteroid explodes
                        break
                    elif toRet[-1] < abs(curr):
                        # this asteroid bigger, explode asteroid and keep looping
                        toRet.pop(-1)
                        if not toRet or toRet[-1] < 0:
                            toRet.append(curr)
                    else:
                        # equal, both explodes and loop ends
                        toRet.pop(-1)
                        break
            i += 1 
        
        return toRet
        