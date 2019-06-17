# -*- coding: utf-8 -*-
"""
Created on June 17 2019
Leetcode: Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Time Complexity O(n), iterate through the array once
Space Complexity: O(1), Need to keep track of sliding window index, current product, and counter. 
@author: bohan
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Approach 1: taking O(n^2) case in worse case:
        counter = 0
        for i in range(len(nums)):
            if nums[i] < k:
                counter += 1

                j = i + 1
                product = nums[i]
                while j < len(nums):
                    if product * nums[j] < k:
                        product = product * nums[j]
                        j += 1
                        counter +=1
                    else:
                        break
            
        return counter


        # Approach 2: Sliding window in O(n) time
        
        if k <= 1:
            return 0

        counter = 0
        currProd = 1
        left = 0

        for right, val in enumerate(nums):
            currProd = currProd * val
            while currProd >= k:
                currProd = currProd / nums[left]
                left+=1
            
            counter += right-left+1
        
        return counter
            
            
        

