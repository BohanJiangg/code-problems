# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:03:20 2019
Leetcode: Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
 
Time Complexity O(n*2), in the worst case where most elements are not in arr2 and need to find each element from arr1 and sort them  
Space Complexity: O(n), counter dict and toRet that stores sorted array. 
@author: bohan
"""


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        if not arr1:
            return arr1
        
        toAppend = sorted([x for x in arr1 if x in list(set(arr1) - set(arr2))])
        
        
        counter = {}
        for num in arr2:
            counter[num] = 0
        
        for num in arr1:
            if num in counter:
                counter[num] += 1
                
        
        toRet = []
        for num in arr2:
            for times in range(counter[num]):
                toRet.append(num)
        
        if toAppend:
            toRet += toAppend
        
        return toRet
        