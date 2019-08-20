# -*- coding: utf-8 -*-
"""
Created on August 20 2019
Leetcode: Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

'''
        Initial Setup:
        T = [73, 74, 75, 71, 69, 72, 76, 73]
        ans = [0, 0, 0, 0, 0, 0, 0, 0]
        stk = []

        1) ans = [0, 0, 0, 0, 0, 0, 0, 0]
           stk = [7]
        2) ans = [0, 0, 0, 0, 0, 0, 0, 0]
        stk = [6]
        3) ans = [0, 0, 0, 0, 0, 1, 0, 0]
        stk = [6, 5]
        4) ans = [0, 0, 0, 0, 1, 1, 0, 0]
        stk = [6,5,4]
        5) ans = [0, 0, 0, 2, 1, 1, 0, 0]
        stk = [6,5,3]
'''

Time Complexity O(n), one-pass
Space Complexity: O(n), keep elements in a stack 
@author: bohan
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        # Using stack
        if not T:
            return None

        ans = [0] * len(T)
        stk = []
        

        for i in range(len(T) - 1, -1, -1):
            while stk and T[i] >= T[stk[-1]]:
                stk.pop()
            if stk:
                ans[i] = stk[-1] - i
            stk.append(i)
        return ans 
        



        
            

        # Time limit exceeded
        # unknown = [0]
        # toRet = [0] * len(T)
        # for i in range(1, len(T)):
        #     curr = T[i]
        #     new = [i]
        #     for idx in unknown:
        #         if curr > T[idx]:
        #             toRet[idx] = i - idx
        #         else:
        #             new.append(idx)
        #     unknown = new
            
        # return toRet