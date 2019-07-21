# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:57:03 2019
Leetcode: Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


Note:
    Each element in the result must be unique.
    The result can be in any order.


Time Complexity O(n*m), need to iterate through all unique values of nums1 and nums2
Space Complexity: O(n), worst case where intersecting array is a subset of the other.  
@author: bohan
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        toRet = []
        for i in nums1:
            if i in nums2:
                toRet.append(i)
        
        return toRet