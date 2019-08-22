# -*- coding: utf-8 -*-
"""
Created on August 22 2019
Leetcode: Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Time Complexity O(n), one-pass through all values of num
Space Complexity: O(n), need to store max potential swap value for every index in memo 
@author: bohan
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        str_num = str(num)
        currMax = int(str_num[-1])
        currIdx = len(str_num) - 1
        memo = [-1] * len(str_num)
        for i in range(len(str_num)-2, -1, -1):
            if int(str_num[i]) < currMax:
                memo[i] = currIdx
            if int(str_num[i]) > currMax:
                currMax = int(str_num[i])
                currIdx = i
        
        str_num = list(str_num)
        for idx1, idx2 in enumerate(memo):
            if idx2 != -1:
                str_num[idx1], str_num[idx2] = str_num[idx2], str_num[idx1]
                return int(''.join(str_num))
        
        return num