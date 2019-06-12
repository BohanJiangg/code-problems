# -*- coding: utf-8 -*-
"""
Created on June 12 2019
Leetcode: Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000


Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        hashTable = {}

        count = 0
        # Indicates length of subarray
        for i in range(1, len(A)+1):
            
            # Indicates number of such contiguous subarrays in A
            for j in range(len(A)):
                if j+i <= len(A): 
                    subSum = 0
                    if i == 1:
                        subSum = A[j]
                    else:
                        subSum = hashTable[(j,j+i-1)] + A[j+i-1:j+i]
                    hashTable[(j,j+i)] = subSum
                    if subSum % K == 0:
                        count += 1
        
        return count


        

        