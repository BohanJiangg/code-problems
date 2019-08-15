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
 

prefixSumsA = [4, 9, 9, 7, 4, 5] K = 5
prefixSumsAModK = [4, 4, 4, 2, 4, 0]
cnt = 0+1+2+0+3+1 = 7

Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000


As is typical with problems involving subarrays, we use prefix sums to add each subarray. Let P[i+1] = A[0] + A[1] + ... + A[i]. Then, each subarray can be written as P[j] - P[i] (for j > i). Thus, we have P[j] - P[i] equal to 0 modulo K, or equivalently P[i] and P[j] are the same value modulo K.


Time Complexity O(n), iterate through A once
Space Complexity: O(N), need to store prefixSumsModK 
@author: bohan
"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        if not A:
            return 0

        prefixSums = [0] 

        for num in A:
            prefixSums.append((prefixSums[-1] + num) % K)
        
        count = collections.Counter(prefixSums)
        # Dict that counts the frequency of each mod from 0 to K-1
        # Ex.: 4: 4 for example input

        toRet = [ (v * (v-1))/2 for v in count.values()]
        return sum(toRet)

        


        

        