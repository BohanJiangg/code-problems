"""
Created on Mon Jun 24 20:33:00 2019

Leetcode: Sqrt(x)

Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.


Time Complexity: O(1), one calculation
Space Complexity: O(1), in-place

@author: bohan
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        return int(float(x)**(0.5))