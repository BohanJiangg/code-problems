# -*- coding: utf-8 -*-
"""
Created on July 29 2019
Leetcode: Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Time Complexity O(n), traverse nums once
Space Complexity: O(n), need to store all sums in a dictionary
@author: bohan
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su-k]
            count[su] += 1
        return ans
        




        # Works but O(n^2) time too slow
        # prefixSums = [0] * len(nums)
        # prefixSums[0] = nums[0]
        # for i in range(1, len(nums)):
        #     prefixSums[i] = prefixSums[i-1] + nums[i]
        
        # toRet = 0
        # for i in range(len(prefixSums)):
        #     j = 0
        #     if prefixSums[i] == k:
        #         toRet += 1
        #     while j < i:
        #         if prefixSums[i] - prefixSums[j] == k:
        #             toRet +=1
        #         j+=1
        
        # return toRet






