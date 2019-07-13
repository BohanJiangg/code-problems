# -*- coding: utf-8 -*-
"""
Created on June 21 2019
Leetcode: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Time Complexity O(n), three iterations needed;
Space Complexity: O(n), need to helper arrays to store max heights from left and from right 
@author: bohan
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height:
            return 0
        
        if len(height) == 1:
            return 0
        
        size = len(height)
        
        leftSize = [0] * size
        leftSize[0] = height[0]
        rightSize = [0] * size
        rightSize[size-1] = height[size-1]
        
        for i in range(1, size):
            leftSize[i] = max(height[i], leftSize[i-1])
        
        for i in range(size - 2, -1, -1):
            rightSize[i] = max(height[i], rightSize[i+1])
        
        water = 0
        for i in range(size):
            water += min(rightSize[i], leftSize[i]) - height[i]
        
        return water
        
        
        
        
        
        
        
        
        
        # Working solution but O(n*max height) time 
#        if not height:
#            return 0
#        
#        maxHeight = max(height)
#        
#        cnt = height.count(maxHeight)
#        while cnt < 2 and maxHeight > 0 :
#            maxHeight -= 1
#            cnt = cnt + height.count(maxHeight)
#    
#        if maxHeight == 0:
#            return 0
#        
#        
#        water = 0
#        
#        for currHeight in range(maxHeight, 0, -1):
#            
#            # Search for first bar of this height
#            left = 0
#            right = 0
#            
#            while left < len(height) and height[left] < currHeight:
#                left += 1
#                
#            right = left
#            
#            while right < len(height): 
#                right += 1
#                
#                while right < len(height) and height[right] < currHeight:
#                    right += 1
#                
#                if right == len(height):
#                    break
#                
#                if right - left > 1:
#                    water += (right - left - 1)
#                    left = right
#                elif right - left == 1:
#                    left = right
#            
#            
#        return water
            
            