
# -*- coding: utf-8 -*-
"""
Created on August 23 2019
Leetcode: Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Time Complexity O(n), one-pass iterate through array 
Space Complexity: O(1), keep track of constants 
@author: bohan
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        maxOnes = 0
        currMax = 0
        consec = False
        for item in nums:
            if item == 1:
                if consec:
                    currMax += 1
                else:
                    consec = True
                    currMax = 1
            else:
                maxOnes = max(maxOnes, currMax)
                consec = False
        maxOnes = max(maxOnes, currMax)
        return maxOnes 