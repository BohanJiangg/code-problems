# -*- coding: utf-8 -*-
"""
Created on July 30 2019
Leetcode: Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Time Complexity O(n log n), sort by starting time 
Space Complexity: O(n), need to make another list of sorted Intervals 
@author: bohan
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals or len(intervals) == 1:
            return True

        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] < sortedIntervals[i-1][1]:
                return False
        return True
