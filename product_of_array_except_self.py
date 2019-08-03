# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:52:58 2019
Leetcode: Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


Time Complexity: O(n), iterate through list twice
Space Complexity: O(n), need toRet of length nums

@author: bohan

"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    if not nums or len(nums) == 1:
        return []
    
    toRet = []
    running_product = 1
    for num in nums:
        toRet.append(running_product)
        running_product *= num
    
    running_product = 1
    for i in range(len(nums)-1, -1, -1):
        toRet[i] *= running_product
        running_product *= nums[i]
    
    return toRet 