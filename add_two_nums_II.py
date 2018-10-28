# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:21:12 2018
Leetcode: Add Two Numbers II
Time Complexity O(m+n+k) time, where m is length of l1, n is length of l2, k is length of l1+l2
Space Complexity: O(k), where k is linked list of length l1 + l2

@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            val1 = val1 + str(l1.val)
        
        val2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            val2 = val2 + str(l2.val)
        
        res = str(int(val1) + int(val2))
        
        resList = ListNode(res[0])
        resHead = resList
        
        for i in range(1, len(res)):
            resList.next = ListNode(res[i])
            resList = resList.next
        
        return resHead
        
        
        