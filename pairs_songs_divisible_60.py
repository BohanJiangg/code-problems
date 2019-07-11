# -*- coding: utf-8 -*-
"""
Created on July 11 2019
Leetcode: Pairs of Songs With Total Durations Divisible by 60

There are two sorted arrays nums1 and nums2 of size m and n respectively.

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

Time Complexity O(n), go through every item once then through dic once
Space Complexity: O(n), need dic storing frequency of modulo items 
@author: bohan
"""

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        output = 0
        dic = {}
        for item in time:
            i = 60 - (item % 60)
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        visited = []
        for key in dic:
            if not key in visited:
                visited.append(key)
                j = 60 - key
                if j in dic and not j == 30:
                    output += dic[key] * dic[j]
                    visited.append(j)

        if 60 in dic:
            for i in range(1, dic[60]):
                output+=i
        if 30 in dic:
            for i in range(1, dic[30]):
                output+=i

        return output
            
        