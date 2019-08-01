# -*- coding: utf-8 -*-
"""
Created on July 29 2019
Leetcode: Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,8],[8,10],[15,18]]
Output: [[1,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Time Complexity O(n^2), worst case where no interval overlaps, need to check for merged in every interval stored in dict 
Space Complexity: O(n), need to store intervals in dict
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
        
        intervals.sort(key=lambda x: x[0])

        merged = {}
        merged[(intervals[0][0], intervals[0][1])] = intervals[0]

        for interval in intervals[1:]:
            inserted = False
            for key, val in merged.items():
                if (key[0]<=interval[0]<=key[1] or key[0]<=interval[1]<=key[1]) or (interval[0]<=key[0]<=interval[1] or interval[0]<=key[1]<=interval[1]):
                    del merged[key]
                    merged[(min(interval[0], key[0]), max(interval[1], key[1])) ] = [min(interval[0], key[0]), max(interval[1], key[1])]
                    inserted = True
                    
            if not inserted:
                merged[tuple(interval)] = interval
        
        return merged.values()
