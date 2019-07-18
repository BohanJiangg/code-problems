# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:19:27 2019

Leetcode: Minimum Number of K Consecutive Bit Flips

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

Time Complexity: O(n), iterate through list once
Space Complexity: O(n), need to store isFlipped list to keep track

@author: bohan

"""

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        res = 0
        flipped = 0
        isFlipped = [0] * len(A)
        
        for i in range(len(A)):
            
            # This represents the closing event
            if (i >= K):
                flipped ^= isFlipped[i-K]
            if flipped == A[i]:
                if i+K > len(A): 
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res+=1
                
        return res
        
        
        
        
        
        
        
        
        # Below solution works but too slow: O(n) time
#        if K > len(A):
#            return -1
#        
#        numZeroes = 0
#        for num in A:
#            if num == 0:
#                numZeroes += 1
#        
#        if numZeroes == 0:
#            return 0
#        
#        if K == 1:
#            return numZeroes
#        
#        if K % 2 == 0 and numZeroes % 2 == 1:
#            return -1 
#        
#        numFlips = 0
#        copy = [i for i in A]
#        for i in range(len(A)):
#            print(copy)
#            if copy[i] == 0:
#                for j in range(K):
#                    if i+j > len(A) - 1:
#                        return -1
#                    else:
#                        if copy[i+j] == 0:
#                            copy[i+j] = 1
#                        else:
#                            copy[i+j] = 0
#                numFlips += 1
#        
#        return numFlips
        
        
        
        
        