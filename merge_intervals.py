# -*- coding: utf-8 -*-
"""
Created on July 29 2019
Leetcode: Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,8],[8,10],[15,18]]
Output: [[1,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        def findMerge(interval, visited):
            

        toRet = []
        visited =[]
        for i in range(len(intervals)):
            interval = intervals[i]
            if not interval in visited:
                toRet.append(findMerge(interval, visited))
