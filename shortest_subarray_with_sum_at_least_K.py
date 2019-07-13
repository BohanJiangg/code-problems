# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:03:41 2019
Leetcode: Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Time Complexity O(n), time, sliding window solution
Space Complexity: O(n), need to store a prefix list and a monoq. 
@author: bohan
"""

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        N = len(A)
        
        # P is list of prefix sums from for A
        P = [0]
        for x in A:
            P.append(P[-1] + x)
            
            
        # Want smallest y-x with Py - Px >= K
        # Let optimal(y) be the largest x such that P[x] <= P[y] - K
        ans = N+1 #impossible max val
        
        monoq = collections.deque() #optimal(y) candidates, represented as indices of P 
        
        for idx, val in enumerate(P):
            # make sure q is increasing
            while monoq and val <= P[monoq[-1]]:
                monoq.pop()
            
            while monoq and val - P[monoq[0]] >= K:
                # update answer for each candidate in monoq and pop
                ans = min(ans, idx - monoq.popleft())
            
            monoq.append(idx)
        
        return ans if ans < N+1 else -1 
            
        
        