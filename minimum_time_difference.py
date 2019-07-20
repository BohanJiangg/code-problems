# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:55:19 2019
Leetcode: Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list. 

Note:

    The number of time points in the given list is at least 2 and won't exceed 20000.
    The input time is legal and ranges from 00:00 to 23:59.

Time Complexity O(n log n), need to sort the times
Space Complexity: O(n), need to store times in integer
@author: bohan
"""

def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        times_min = []
    
        for ele in timePoints:
            curr = ele.split(':')
            hours = int(curr[0])*60
            minutes = int(curr[1])
            times_min.append(hours+minutes)
        
        
        times_min.sort()
        
        min_diff = float('inf')
        
        
        for i in range(1, len(times_min)):
            diff = times_min[i] - times_min[i-1]
            if diff < min_diff:
                min_diff = diff
        
        
        diff = times_min[0] + 1440 - times_min[-1]
        
        if diff < min_diff:
            min_diff = diff
        
        
        return min_diff


    
    