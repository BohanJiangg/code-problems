# -*- coding: utf-8 -*-
"""
Created on September 5 2019
Leetcode: Last Stone Weight

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Time Complexity: O(n*n log n), iterate through stones, sorting every time
Space Complexity: O(1), always compare two stones 

@author: bohan

"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        while stones:
            stones.sort()
            first = stones.pop(-1)
            second = stones.pop(-1)
            if first > second:
                stones.append(first-second)
            
            if not stones:
                return 0
            elif len(stones) == 1:
                return stones.pop()

            

        