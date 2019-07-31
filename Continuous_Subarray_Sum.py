# -*- coding: utf-8 -*-
"""
Created on July 31 2019
Leetcode:  Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

Time Complexity O(n^2), in the worst case where we iterate through entire prefix sums and substract from it 
Space Complexity: O(n), need prefixSums of length nums
@author: bohan
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        

        prefixSums = [nums[0]] + [0] * (len(nums)-1)
        for i in range(1, len(nums)):
            prefixSums[i] = nums[i] + prefixSums[i-1]


        for i in range(1, len(prefixSums)):
            if i >= 1:
                if k == 0 and prefixSums[i] == k:
                    return True
                elif k != 0 and prefixSums[i] % k == 0:
                    return True
            for j in range(0, i-1):
                if k == 0 and (prefixSums[i] - prefixSums[j]) == k:
                    return True
                elif k != 0 and (prefixSums[i] - prefixSums[j]) % k == 0:
                    return True
        return False





        
        