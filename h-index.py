# -*- coding: utf-8 -*-
"""
Created on September 9 2019
Leetcode: H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.


Time Complexity: O(n log n), need to sort citations
Space Complexity: O(n), sort

@author: bohan

"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        if not citations: 
            return 0
        
        citations.sort()
        # citations = [0,1,3,5,6]
        n = len(citations)
        for i in xrange(n):
            if citations[i] >= (n-i):
                return n-i
        return 0