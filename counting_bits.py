# -*- coding: utf-8 -*-
"""
Created on July 26 2019
Leetcode: Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Time Complexity O(n^2), counting binary conversions for every number
Space Complexity: O(n), need to store all nums from 0 to num
@author: bohan
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        if num == 0:
            return [0]
        if num == 1:
            return [0,1]

        nums = [0,1] + [[None]] * (num-1)

        for i in range(2, len(nums)):
            nums[i] = str(bin(i)).count('1') 
        
        return nums
        