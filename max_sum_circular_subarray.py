# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:43:00 2019

Leetcode: Maximum Sum Circular Subarray

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)


Time Complexity: O(n),
Space Complexity: O(n),  

@author: bohan

"""

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        expandedA = A + A[0:len(A)]
        
        
        
        
        
        
        
        
# Solution works but too slow: O(n^2) time       
#        maxSum = max(A)
#        
#        expandedA = A + A[0:len(A)]
#        
#        # indicates length of subarray
#        for i in range(2, len(A)+1):
#            for j in range( len(expandedA) - i ):
#                
#                if sum(expandedA[j:j+i]) > maxSum:
#                    maxSum = sum(expandedA[j:j+i])
#                
#                if len(expandedA[j:j+i]) == len(A):
#                    break
#        
#        return maxSum