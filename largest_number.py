# -*- coding: utf-8 -*-
"""
Created on August 6 2019
Leetcode: Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

Time Complexity O(n log n), need to custom sort nums string 
Space Complexity: O(n), creates copy of nums
@author: bohan
"""

class Solution(object):
    import functools
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        num = [str(x) for x in nums]
        num.sort(key = functools.cmp_to_key(lambda b, a: ((a+b)>(b+a))-((a+b)<(b+a)) ))
        return ''.join(num).lstrip('0') or '0'