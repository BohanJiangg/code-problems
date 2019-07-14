# -*- coding: utf-8 -*-
"""
Created on July 11 2019
Leetcode: Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums2: List[int]
        :rtype: float
        :type nums1: List[int]
        """
        
        # Case where either nums1 or nums2 is empty
        if not nums1:
            if len(nums2) % 2 == 1:
                return nums2[int(len(nums2)/2)]
            else:
                return (nums2[int(len(nums2)/2)] + nums2[int(len(nums2)/2)-1])/2
            
        if not nums2:
            if len(nums1) % 2 == 1:
                return nums1[int(len(nums1)/2)]
            else:
                return (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1])/2
        
        
        