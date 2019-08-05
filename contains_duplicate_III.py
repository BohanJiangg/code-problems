# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:33:04 2019

Leetcode: Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true


Time Complexity: O(n), one-pass
Space Complexity: O(k), need to store last k elements 

@author: bohan


"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        for i, v in enumerate(nums):
            # In case where t = 0
            bucketNum, offset = (int(v / t), 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # In case where t = 0
                del buckets[int(nums[i - k] / t) if t else nums[i - k]]

        return False
            
            
            
            
            
            
            