# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:07:35 2019
Leetcode: Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Time Complexity: O(n),
Space Complexity: O(n),  

@author: bohan

"""
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights = w
        self.prob_dist = []
        total = sum(w)
        self.prob_dist.append((0, float(w[0])/total))
        for i in range(1, len(w)):
            self.prob_dist.append((self.prob_dist[i-1][1], self.prob_dist[i-1][1] + float(w[i])/total))

    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.random()
        for idx, tup in enumerate(self.prob_dist):
            if tup[0] <= num < tup[1]:
                return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()