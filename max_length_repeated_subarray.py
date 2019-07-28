# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:23:13 2019
Leetcode: Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].


Time Complexity: O(len(A)*len(B)), iterate through B once for each A
Space Complexity: O(len(A)*len(B)), need A*B matrix for dp   

@author: bohan

"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        
        dp = [ [0] *(len(B)+1) for i in range(len(A)+1)]
        ans = 0
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    ans = max(ans, dp[i][j])
        
        return ans
                