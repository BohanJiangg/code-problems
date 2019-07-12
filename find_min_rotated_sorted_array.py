# -*- coding: utf-8 -*-
"""
Created on July 12 2019
Leetcode: Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Time Complexity O(n/2) = O(n), because in the worst case we go through half the array.
Space Complexity: O(1), with 2 ptrs
@author: bohan
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        leftPtr = 0
        rightPtr = len(nums) -1
    
        curr = nums[rightPtr]
        if nums[leftPtr] < nums[rightPtr]:
            curr = nums[leftPtr]
            
        if len(nums) == 2:
            return curr

        goRight = True
        if leftPtr+1 < len(nums) and rightPtr-1 >= leftPtr +1:
            if nums[leftPtr+1] < nums[rightPtr-1] and nums[leftPtr+1] < curr:
                curr = nums[leftPtr+1]
                leftPtr+=1
            elif nums[rightPtr-1] < nums[leftPtr+1] and nums[rightPtr-1] < curr:
                curr = nums[rightPtr-1]
                rightPtr -=1
                goRight = False
            elif rightPtr-1 == leftPtr+1 and nums[leftPtr+1] < curr:
                curr = nums[rightPtr-1]

        if len(nums) == 3:
            return curr

        if goRight:
            while leftPtr+1 < rightPtr-1 and nums[leftPtr+1] < curr:
                leftPtr += 1
                curr = nums[leftPtr]
        else: 
            while rightPtr-1 > leftPtr +1 and nums[rightPtr - 1] < curr:
                rightPtr -= 1
                curr = nums[rightPtr]



        return curr
                

        


        
        