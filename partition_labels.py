# -*- coding: utf-8 -*-
"""
Created on September 10 2019
Leetcode: Partition List

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.



Time Complexity: O(n), store in dict and iterate through S once
Space Complexity: O(n), need to store last occurence of char in dict

@author: bohan

"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return 0
        if len(S) == 1:
            return [1]
        
        last = {char: idx for idx, char in enumerate(S)}

        anchor = j = 0
        sizes = []

        for idx, char in enumerate(S):
            j = max(j, last[char])
            if idx == j:
                sizes.append(j - anchor + 1)
                anchor = idx + 1
        
        return sizes
            

        

        

            

        