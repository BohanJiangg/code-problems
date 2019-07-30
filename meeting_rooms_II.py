# -*- coding: utf-8 -*-
"""
Created on July 30 2019
Leetcode: Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

Input: [[9,10],[4,9],[4,17]]
Ouput: 2

Time Complexity O(n log n), need to sort array
Space Complexity: O(n), min-heap contains N elements in worst case
@author: bohan
"""

class Solution(object):
    import heapq
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        sortedIntervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        endTimes = [sortedIntervals[0][1]]
        rooms = 1

        for i in range(1, len(sortedIntervals)):
            if endTimes and sortedIntervals[i][0] < endTimes[0]:
                rooms+=1
                heapq.heappush(endTimes, sortedIntervals[i][1])
            else:
                heapq.heappop(endTimes)
                heapq.heappush(endTimes, sortedIntervals[i][1])
        return rooms

        